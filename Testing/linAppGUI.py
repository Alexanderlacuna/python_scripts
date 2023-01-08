import gi
import subprocess
import multiprocessing
import os
import glob
import re
import sys

from subprocess import Popen, PIPE

from PIL import Image

gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gtk
from gi.repository.GdkPixbuf import Pixbuf

# This gui tool displays icons from freedesktop desktop entry files

# Note: .desktop files must be located in the defaultAppDir!

 
keyList = [ 'Name', 'Categories', 'Exec', 'Icon', 'Actions' ]

#default directory for desktop entry file location

defaultAppDir =  "/usr/share/applications/"

dictionary = {}

#
def fillIconView(gtkBuilder, desktopEntryData, listStore):
    scrolledwindow = gtkBuilder.builder.get_object("scrolled_window")
 
    fullListStore = populateListStore(listStore,desktopEntryData, 0)      
    iconView = gtkBuilder.builder.get_object("icon_view")
    iconView.set_model(fullListStore)
    iconView.set_pixbuf_column(0)
    iconView.set_text_column(1)
    iconView.set_tooltip_column(2)
    iconView.set_text_column(3)   



#window main sets up gui widgets
class WindowMain():

    def __init__(self):
       


        # Get GUI Glade file
        self.builder=Gtk.Builder()
        self.builder.add_from_file("linappGUI.glade")
        self.builder.connect_signals(self)
                
        # Display main window
        self.windowMain=self.builder.get_object("window_main")
        self.windowMain.show_all()
        


        guestOneAppData = getMetadataDictionary(defaultAppDir, "appbox", keyList)

        listStore = self.builder.get_object("list_store")
        fillIconView(self, guestOneAppData, listStore)


        print (getIconThemePath("firefox"))
        
    def item_activated(self,listStore, treePath):
        
        execCmd = f"{listStore[treePath][1]}"      
                                                            
        os.popen(f"{execCmd}")  

      
    
    def on_window_main_destroy(self, widget, data=None):
        print("on_window_main_destory")
        Gtk.main_quit()


    def on_ubuntu_clicked(self, widget):
        guestAppData = getMetadataDictionary(defaultAppDir, "ubuntu", keyList)
        listStore =  self.builder.get_object("list_store")
        listStore.clear()
        fillIconView(self, guestAppData, listStore)


    def on_fedora_clicked(self, widget):
        guestAppData = getMetadataDictionary(defaultAppDir, "fedora", keyList)
        listStore =  self.builder.get_object("list_store")
        listStore.clear()
        fillIconView(self, guestAppData, listStore)

    def on_btn3_clicked(self, widget):
        listStore =  self.builder.get_object("list_store")
        listStore.clear()

        guestAppData = getMetadataDictionary(defaultAppDir, "ubuntu", keyList)        
        fillIconView(self, guestAppData, listStore)

        guestAppData = getMetadataDictionary(defaultAppDir, "fedora", keyList)        
        fillIconView(self, guestAppData, listStore)


    def main(self):
        Gtk.main()

#calls on the extractData module to extract desktop entry file data, this is metadata about guest apps
def getMetadataDictionary(directory, prefix, keyList):
    
    metadataDictionary = {}    
    iterator = glob.iglob(f"{directory}{prefix}-*.desktop")  #searches for files prefixed with appbox- with the .desktop file extention
    for path in iterator :
        
        if path not in metadataDictionary: #TODO metadataDictionary is not going to have prior data under current set up and will be empty      
            data = extractData(keyList, path)
            if data != {}:
                metadataDictionary.update( {f'{path}': data} )                

    return metadataDictionary

#populates listStore with details from application meta data
#It also stores an application icon image to the listStore which along with the details can then be displayed in the gtk iconView
def populateListStore(listStore, data, count):
    listStore.clear()
    
    for path in data:
        count += 1
        if count > 24:
           break
            
        try:
            iconStr = data[path]["Icon"][0]
            if iconStr[0] == '/':
                if os.path.isfile(iconStr):                    
                    pixelBuffer = Image.open(iconStr)

            else:    
                print (iconStr)
                pixelBuffer = Gtk.IconTheme.get_default().load_icon(iconStr, 48, 0)

            lable = data[path]["Name"][0].replace(" (AppBox)", "")  #remove the (appBox) tag from app name

            execCmd = re.sub(' %u','',data[path]["Exec"][0], flags=re.IGNORECASE)
                     
            listStore.append([pixelBuffer, f"{execCmd}", "tool-tip", lable]) #
                
        except:
            print (f"")

    return listStore

#returns the theme of host or gtk default theme
def getIconThemePath(iconName):

    iconTheme = Gtk.IconTheme.get_default()
    iconInfo = iconTheme.lookup_icon(iconName, 48, 0)
    
    #if iconInfo != None:
        #filePath, filename = os.path.split(iconInfo.get_filename())
    return iconInfo.get_filename()

# Extracts relevant data from .desktop files
# .desktop files contain app metadata on xdg conforming desktop systems 
# xdg/freedesktop: (most linux desktop environments fully comply, all most all partially comply or have compatibility modules)
# on systems that do not comply LinuxAppBox still makes use of these files for its own purposes
# on non-conforming systems guest apps may not be discoverable by the host operating system

#checks if icon is present on system
def iconIsMissing(iconName):
    if iconName[0] == '/':
        if os.path.isfile(iconName):
            print(f"System Icon {iconName} was Found") 
            return False
    try:
        pixbuf = Gtk.IconTheme.get_default().load_icon(iconName, 48, 0)
        if not pixbuf:
             print(f"System Icon {iconName} not Found") 
             return True
        return False               
    except gi.repository.GLib.Error:
        print(f"System Icon {iconName} not Found") 
        return True

#extracts data from desktop entry files
def extractData(keyList, filePath):
    data = {}
    with open(filePath) as desktopFile:       # Open file
        #check if there is a current value in data dictionary 
        if data.get(filePath) == None:
            pass  #If value exists there's no reason anything but identical data should be expected so pass to skip this file
        fileData = {}
        for line in desktopFile:   # Get line of file
            if "[Desktop Action" in line:
                return data

            for key in keyList:    # Get key of data dictionary
                success = False

                entry = re.findall(f"^{key}=", line)           # Regex search line of file for a string that matches data dictionary key

                if entry:                                        # when a match is found: remove line end,
                                                                 # then remove the key to give a newValue to record in data dictionary
                    success = True
                    removeEndLine = line.replace('\n','')                
                    newValue = re.sub(r'^.*?=', '', removeEndLine)

                    if key == "Icon":
                        if iconIsMissing(newValue): 
                            success = False
           
                if success:
                         
                    if newValue != "None":
                        if newValue.find(';') > -1:
                            listItem = newValue.split(';')
                        else:
                            listItem = [f"{newValue}"]          
                        fileData[key] = listItem

                    data.update(fileData)

        return data

     


if __name__ == "__main__":
    application=WindowMain()
    application.main()

import os
import time
import sys
import re
import subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

#sys.argv[1] = File Source
#sys.argv[3] = File Extension
#sys.argv[2] = getDestination dir


#this pythpn file should be ran with three args, 1 a source dir, 2 a file extension, 3 a destination

#the module looks for changes in the dest dir, in files with the extension, so it can move them to the destination (last part is not yet implemented)

def getWatchedDir():

    return sys.argv[1] # "/home/user/Downloads/Main/"

def getDestDir():

    return sys.argv[2] # "/home/user/Downloads/Main/"

def getFileExtension():

    return sys.argv[3] # "/home/user/Downloads/Main/"



def distroboxCreateImage(source, name, init, preInitHooks, initHooks, volume, additionalFlags):

    subprocess.run(f"distrobox-create --image {source} {init} --pull --yes --name {name} {preIniteHooks} {initHooks} {volume} {additionalFlags}", shell=True)

def distroboxCreateClone(origional, name, init, preInitHooks, initHooks, volume, additionalFlags):

    subprocess.run(f"distrobox-create --clone {origional} {init} --pull --yes --name {name} {initHooks} {volume} {additionalFlags}", shell=True)

def distroboxRemoveImage(name):

    subprocess.run(f"distrobox-rm {name} --yes --force", shell=True)

def distroboxEnter(command, args):

    subprocess.run(f"distrobox-enter {args} {name}", shell=True)

def distroboxList():

    subprocess.run(f"distrobox-list", shell=True)

def distroboxList(name):

    subprocess.run(f"distrobox-stop {name} --yes", shell=True)

def execute(command):

    subprocess.run(f"{command}", shell=True)


def getDataString(filePath, key):

    dataStr = ""
    with open(filePath) as desktopFile:       # Open file
        #check if there is a current value in data dictionary 
        for line in desktopFile:   # Get line of file
            
            if "[Desktop Action" in line:
                print ("END")
                return data
            success = False                
            entry = re.findall(f"^{key}=", line)           # Regex search line of file for a string that matches data dictionary key

            if entry:                                        # when a match is found: remove line end, and remove the key to give a newValue to record in data dictionary
                success = True
                removeEndLine = line.replace('\n','')                
                newValue = re.sub(r'^.*?=', '', removeEndLine)
          
            if success:                
                if newValue != "None":
                    if newValue.find(';') > -1:
                        listItem = newValue.split(';')
                    else:
                        listItem = newValue         
                    dataStr = listItem
             
    
    return dataStr
     

   
#triggers if file is created
def onCreated(event):
    
    srcPath = event.src_path
    if os.path.isfile(srcPath):
        if sys.argv[3] in srcPath: 
            filePath,fileName  = os.path.split(event.src_path)  

              print(f"File Created: {fileName}")
 



def onDeleted(event):
    if sys.argv[3] in event.src_path:   
        srcPath = os.path.split(event.src_path)
        print(f"File Deleted: {srcPath[1]}")
        # ToDo create appbox-Data file
        # check appbox-Data if app exists on host
        # delete appData file on host! [ distrobox-export --app <AppName> --delete  -ep sys.argv[2] ]


def onMoved(event): 
   
    if "bak" in event.src_path:
        return

    if sys.argv[3] in event.src_path:
        #print(f"{event.src_path}\n{event.dest_path}")         
        srcPath, oldName = os.path.split(event.src_path)
        newPath, newName = os.path.split(event.dest_path)
        if srcPath != newPath:
            print(f"File {oldName} Moved \n From: {srcPath} To: {newPath}")
        if oldName != newName:
            print(f"File Renamed\nFrom: {oldName} To: {newName}")
            #os.popen(f"cp {newPath}/{newName} {sys.argv[2]}")               
            #os.popen(f"cp {newPath}/{newName} bak-{newName}")

            iconStr = getDataString(event.dest_path, 'Icon')
            
            subprocess.run(f"distrobox-export --app {newName} --force --icon {iconStr} --export-path {sys.argv[2]}", shell=True)   
            #os.popen(f"mv {newPath}/{newName} {sys.argv[2]}")    
      
        elif ".txt" in newName:
            print(f"File Edited: {newName}")
            os.popen(f"cp {newPath}/{newName} {sys.argv[2]}")     




if __name__ == "__main__":

    patterns = ["*"]
    ignorePatterns = None
    ignoreDirs = True
    caseSensitive = True
    handler = PatternMatchingEventHandler(patterns, ignorePatterns, ignoreDirs, caseSensitive)

    handler.on_created = onCreated
    handler.on_deleted = onDeleted
    handler.on_moved = onMoved

    
    
    

    watchedDir = getWatchedDir()

    observer = Observer()
    observer.schedule(handler, watchedDir, recursive=True)

    observer.start()

    #subprocess.run(f"sudo apt-get install gtkterm -y", shell=True) 

    try:
        if len(sys.argv) < 3:
            print("Missing file extention argument\n")
            exit(0)
        print(f"Python Watchdog Running in {watchedDir}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting!")
        observer.stop()
        observer.join()





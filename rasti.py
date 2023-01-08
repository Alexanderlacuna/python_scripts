
import csv
def parse_line_csv(line):
    return_list = line.split('","')
    return_list[-1] = return_list[-1][:-2]
    return_list[0] = return_list[0][1:]
    return return_list





with open("/home/kabui/Music/text_files/ty.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for line in csv_reader:
    	lx = line 
    	breakpoint()

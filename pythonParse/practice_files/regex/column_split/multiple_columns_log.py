''' Testing getting columns in python regex'''
import re

import csv
csv_columns = ['Id', 'Name','Person_To','Date','Time','Message','Said_Yes', 'Said_No']
csv_file = "Messages.csv"
message_number = 1
# sample line =
#February 16, 2021           4:37:13 PM      from Sarah Jiang to All Participants:       Thank you!

#NEEDS WORK WITH DATE BUT ALL LINES ARE OFFICIALLY INFERENCED!!!

# February 16, 2021           EOF
date_string = "\S+\s\d+,\s\d+" # This one is more specific but only works online simulator
time_string = "\d:\d+:\d+\s\S+"
person_from_string = r"\bfrom\s(.+)\sto\b"
person_to_string = r"\bto\s(.+):" 
message_string = r"\b:\s+(.+)"

splitter = "\t"
#making first columns for csv (without any inferencing, straight regex)
def parse_line(line_string, msg_num):
	my_dict = {}
	line_string = re.sub("\x00", "", line_string)
	if(line_string):
		parts = re.split(splitter, line_string)
		if len(parts) >= 3:
			message = parts[3]
			my_dict['Message'] = message 
			messages = message.lower()
			strings = messages.split(" ")
			if "yes" in strings:
				my_dict['Said_Yes'] = 1
			else: 
				my_dict['Said_Yes'] = 0
			if "no" in strings:
				my_dict['Said_No'] = 1
			else: 
				my_dict['Said_No'] = 0
		if len(parts) >= 2:
			people = parts[2].strip().split("to")
			my_dict['Name'] = people[0][5:].strip()
			my_dict['Person_To'] =  people[1][:-1].strip()
			my_dict['Time'] = parts[1].strip()
		if len(parts) >= 1:
			my_dict['Id'] = msg_num
			my_dict['Date'] = parts[0].strip() 
		if parts:
			return my_dict
		return None
	return None
	

# FILES IN CURRENT DIRECTORY -----> WORKING
#Note THAT THIS ONE IS THIS DIRECTORY
import os
import glob
writer = None
file_num = 1
try:
	with open(csv_file, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
		writer.writeheader()


		for filename in glob.glob('*.txt'):
			line_number = 0
			#opening csv file
			with open(os.path.join(os.getcwd(), filename),encoding="utf8", errors='ignore') as f: # open in readonly mode	
				for line_txt in f:
					# using regex to filter whitespaced lines
					first_line = line_txt.split("\n")[0]
					if first_line != '\x00':
						check_phrase = parse_line(first_line, message_number)
						if check_phrase != None:
							print("added message number " + str(message_number) + " to dict")
							writer.writerow(check_phrase)
						message_number += 1
					line_number += 1 
			file_num += 1
	
except IOError:
	print("I/O error")
   	
   	

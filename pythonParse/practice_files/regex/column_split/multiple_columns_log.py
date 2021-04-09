''' Testing getting columns in python regex'''
import re



# sample line =
#February 16, 2021           4:37:13 PM      from Sarah Jiang to All Participants:       Thank you!

#NEEDS WORK WITH DATE BUT ALL LINES ARE OFFICIALLY INFERENCED!!!

# February 16, 2021           EOF

# i didn't change your date string, just created a new one
date_string_test = r'[(d{20}\w{2},\d{4})]'
date_string = "\S+\s\d+,\s\d+"
time_string = "\d:\d+:\d+\s\S+"
person_from_string = r"\bfrom\s(.+)\sto\b"
person_to_string = r"\bto\s(.+):" 
message_string = r"\b:\s+(.+)"

#making first columns for csv (without any inferencing, straight regex)
def parse_line(line_string):
	date_str = re.findall(date_string_test, line_string)
	if date_str:
		print("line == " + str(line_string) )	
		print(date_str)
		return(1)
	return 0






# FILES IN CURRENT DIRECTORY -----> WORKING
#Note THAT THIS ONE IS THIS DIRECTORY
import os
import glob
file_num = 1
for filename in glob.glob('*.txt'):
	line_number = 0
	with open(os.path.join(os.getcwd(), filename),encoding="utf8", errors='ignore') as f: # open in readonly mode	
		for line_txt in f:
			# using regex to filter whitespaced lines
			first_line = line_txt.split("\n")[0]
			if first_line != '\x00':
				print(first_line)
				check_phrase = parse_line(line_txt)
				if check_phrase == 1:
					print("substituted on file_num=" + str(file_num) + ", line_number=" + str(line_number))
			line_number += 1 
	file_num += 1

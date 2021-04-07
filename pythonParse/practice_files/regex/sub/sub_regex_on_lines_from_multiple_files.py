''' Testing sub in python regex'''
import re


phrase_to_look_for = "    "
string_to_place = "GOOFY"




def parse_line(line_string):
	x = re.sub(phrase_to_look_for, string_to_place, line_string)
	if x:
		print("line == " + str(line_string) )	
		print(x)
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
			check_phrase = parse_line(line_txt)
			if check_phrase == 1:
				print("substituted on file_num=" + str(file_num) + ", line_number=" + str(line_number))
			line_number += 1 
	file_num += 1

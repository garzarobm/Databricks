''' Testing split in python regex'''
import re

file_name = "sample_log_file_with_no_carriage_return.txt"

phrase_to_parse = "sample_log_file.txt"

print("searching in " + file_name )
print("searching for phrase=" +phrase_to_parse + "/  in line\n\n\n" )

def parse_line(line_string):
	
	print(phrase_to_parse)
	x = re.findall(phrase_to_parse, line_string)
	print(x)
	return 0










# getting file
f = open(file_name, encoding="utf8", errors='ignore')

id = 0
# going through lines
for x in f:
  parse_line(x)
  id += 1

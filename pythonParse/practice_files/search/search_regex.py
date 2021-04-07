import re

file_name = "findall_regex_with_file_input.txt"

phrase_to_parse = "Spain"



def parse_line(line_string):
	
	print(phrase_to_parse)
	x = re.findall(phrase_to_parse, line_string)
	print(x)
	return 0










# getting file
f = open(file_name, "r")

id = 0
# going through lines
for x in f:
  parse_line(x)
  id += 1

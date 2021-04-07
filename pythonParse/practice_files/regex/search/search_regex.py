''' Testing search in python regex'''
import re

file_name = "sample_log_file_with_no_carriage_return.txt"

phrase_to_parse = "t"

print("searching in " + file_name )
print("searching for phrase='" +phrase_to_parse + "'  in line\n\n\n" )

def parse_line(line_string):
	x = re.search(phrase_to_parse, line_string)
	if x:
		print("line == " + str(line_string) )	
		print(x.start())
		return(1)
	return 0










# getting file
f = open(file_name, encoding="utf8", errors='ignore')

id_num = 0
# going through lines
for x in f:
  found_phrase = parse_line(x)
  if found_phrase  == 1:
    print("found phrase at line=" + str(id_num))
  id_num += 1

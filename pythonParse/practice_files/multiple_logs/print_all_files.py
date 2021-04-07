''' This will be used to inference all files within one folder'''

''' with os ---------> NOT WORKING YET
import os

for filename in os.listdir("../folder_with_logs"):
	print(str(filename)
	#with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode

'''


# FILES IN CURRENT DIRECTORY -----> WORKING
#Note THAT THIS ONE IS THIS DIRECTORY
import os
import glob
for filename in glob.glob('*.txt'):
	with open(os.path.join(os.getcwd(), filename),encoding="utf8", errors='ignore') as f: # open in readonly mode
		for line_txt in f:
			print(line_txt)

''' #FILES IN DIFFERENT PATH ---------> NOT WORKING 
import os
import glob
print(os.getcwd())
path = os.getcwd() + '/../folder_with_logs/'
print(path)
for filename in glob.glob(os.path.join(path, '*.txt')):
	print(str(filename))
	with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
		for line_txt in f:
			print(line_text)
'''

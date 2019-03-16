# roster_dictionary.py
import re
input_file = open('roster_raw.txt', 'r')

input_file_contents = input_file.read() # one string containing entire file
 

student_pattern = re.sub(r' ', r'',input_file_contents)



print (student_pattern)








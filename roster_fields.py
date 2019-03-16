# roster_fields.py
import re 
 
input_file = open('cs176roster.webadvisor.txt', 'r')

input_file_contents = input_file.read() # one string containing entire file
 
 #student pattern contains a regex that extracts one student:
student_pattern = re.compile(r'.+?, .+?\n[0-9]{7}\n[s][0-9]{7}[@][a-z]{8}[.][a-z]{3}\n[A-Z]{2,3}\n[0-9]{2}\n[A-Z]{1}[.][ A-Z]{2}[a-z^A-Z^ A-Z]{0,10}\n')
#								.+?  			 =	last name
#									,            =  comma space
#								     .+?		 =  first name and middle initial
#										\n		 =  newline
#										[0-9]{7} =	student id	
students = student_pattern.findall(input_file_contents) #list
 
output_file = open('roster,txt', 'w')

for student in students:
	#print(re.sub(r'\n', ', ', student))
	print(re.sub(r'\n[s][0-9]{7}[@][a-z]{8}[.][a-z]{3}', ',', student))
	output_file.write(student)
	
output_file.close()

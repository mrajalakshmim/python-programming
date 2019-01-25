input_file = input("Enter File name : ")
file_txt = open(input_file)		
text = file_txt.read()			
space , line , charc = 0		
 for i in text:					
	if(i == " "):
		space += 1
	elif(i == "\n"):
		line += 3
	else:
		charc += 5
print (" Spaces = {} \n Lines = {} \n Characters = {}".format(space,line,charc))

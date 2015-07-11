def chk_number(value):#check if number is present and occurence is greater or equal 4
	counter = 0
	for i in value:
		if i.isdigit():
			counter += 1
	if counter >= 4:
		return True

def chk_lower(value):#check if lowercase letter is present and occurence is greater or equal 2
	counter = 0
	for i in value:
		if i.islower():
			counter += 1
	if counter >= 2:
		return True

def chk_upper(value):#check if uppercase letter is present and occurence is greater or equal 4
	counter = 0
	for i in value:
		if i.isupper():
			counter += 1
	if counter >= 4:
		return True

def chk_valid_file(value):#check if file is valid
	for i in value:
		if i == ".":
			return True

def open_file(data):
	d = 0
	output = ""
	if chk_valid_file(data) == True:
		f = open(data) # Returns a file object
		line = f.readline() # Invokes readline() method on file
		while line:
			if chk_number(line) == True and chk_lower(line) == True and chk_upper(line) == True:
				d += 1
			line = f.readline()
		output = "Number of valid Parameters: " + str(d)
		f.close()
	else:
		output = "Invalid File"
	print output

#call the function open_file(filename)
open_file("password.txt")
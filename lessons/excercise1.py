word = raw_input("Enter an English Word: ")
if(word.isalpha()):
	wordlen = len(word)
	val1 = word[1:wordlen]
	val2  = word[0]
	val3 = str(val1) + str(val2) + "ay"	
	print val3
else:
	print "Invalid Word"
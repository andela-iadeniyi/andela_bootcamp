#CREDITCARD VALIDATOR
def card(number):
	output = ""
	if len(number) == 16:
		rev = number[::-1]
		for i in rev:
			if i%2 == 0:
				output += i + i
			else:
				output += i
	else:
		output = "Invalid CREDITCARD"
	print output
card("12344555")
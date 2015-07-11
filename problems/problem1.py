import webbrowser
import time

count = 0
while count < 3:
	count += 1
	webbrowser.open('google.com')
	time.sleep(5)

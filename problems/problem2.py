import webbrowser
import time
 
def goto_urls(delay, url_value):
	init_delay = 0;
	for i in url_value:
		init_delay += delay
		time.sleep(init_delay)
		webbrowser.open(i)
goto_urls(10, ['google.com', 'yahoo.com', 'gmail.com'])
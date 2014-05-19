def get_page(url):
	''' Take the input as URL and return the HTML page '''
	try:	
		import socket
# Use to set the default time out
		import urllib2
		#socket.setdefaulttimeout(10000000000)
	    	link = urllib2.urlopen(url).read()
		return link
	except:
		return ""
#print get_page("http://www.mmw.net63.net")


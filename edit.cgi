#!/usr/bin/python

import Cookie
import os
import cgi
import cgitb; cgitb.enable() # Optional; for debugging only

cookie = Cookie.SimpleCookie()
lastFilename = ""
try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	filenames = cookie["filenames"].value
	filenames = filenames.split(",")
	lastFilename = filenames[len(filenames)-1]
except Exception, e:
	pass

print("Content-type: text/html\r\n\r\n")

print("""
	<html>
		<body>
		
		<form action="/editing.cgi" method="post">
	""")
	
print("""<img src="/files/%s" alt="" />""" % lastFilename)

print("""
	<input name="action" type="submit" value="filter1" />
	<input name="action" type="submit" value="filter2" />
	<input name="action" type="submit" value="filter2" />

	<input name="action" type="submit" value="text top" />
	<input name="action" type="submit" value="text bottom" />

	<input name="action" type="submit" value="undo" />
	<input name="action" type="submit" value="discard" />
	<input name="action" type="submit" value="finish" />
	</form>
	</body>
	</html>
	""")
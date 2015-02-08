#!/usr/bin/python

# save file
# add to cookie

import Cookie
import os
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:

	# strip leading path from file name to avoid directory traversal attacks
	fn = os.path.basename(fileitem.filename)
	
	if not os.path.exists(os.path.dirname('files/' + fn)):
		os.makedirs(os.path.dirname('files/' + fn))

	open('files/' + fn, 'wb').write(fileitem.file.read())
	message = 'The file "' + fn + '" was uploaded successfully'

	cookie = Cookie.SimpleCookie()
	try:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	except Exception, e:
		pass

	cookie["filenames"] = fn

	print("Location: edit.cgi")
	print cookie
	print("\r\n\r\n")

else:
	print("Content-type: text/html\r\n\r\n");
	print("HIHI! No file was uploaded")
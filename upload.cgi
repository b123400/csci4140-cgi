#!/usr/bin/python

# save file
# add to cookie

import Cookie
import os
import cgi
import cgitb; cgitb.enable()
import subprocess

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:

	# strip leading path from file name to avoid directory traversal attacks
	fn = os.path.basename(fileitem.filename)

	identifyCommand = "identify %s" % fn
	p = subprocess.Popen(identifyCommand, shell=True, stdout=subprocess.PIPE)
	output = p.communicate()[0]
	#output = subprocess.check_output(fileitem.filename, shell=True)
	output = output.split(" ")
	imageFormat = output[1].lowercase
	extension = fileitem.filename.split(".")[-1].lowercase

	ok = False
	if imageFormat == "png" or imageFormat == "gif" or imageFormat == "jpg":
		ok = True
	if extension != imageFormat:
		ok = False
	if not ok :
		print("Content-type: html/text\r\n\r\n")
		print("wrong format")
		exit(0)

	outpath = "files/"+fn

	if not os.path.exists(os.path.dirname(outpath)):
		os.makedirs(os.path.dirname(outpath))

	open(outpath, 'wb').write(fileitem.file.read())
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
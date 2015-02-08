#!/usr/bin/python

import Cookie
import os
import cgi
import cgitb; cgitb.enable() # Optional; for debugging only
import subprocess

arguments = cgi.FieldStorage()

cookie = Cookie.SimpleCookie()
filenames = []
try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	filenames = cookie["filenames"].value
	filenames = filenames.split(",")
except Exception, e:
	pass

def deleteFile(filename):
	os.remove('files/'+filename)

if arguments["action"].value == "discard":

	for filename in filenames:
		deleteFile(filename)

	cookie["filenames"] = ""
	print("Location: index.cgi")
	print(cookie)
	print("\r\n\r\n")

elif arguments["action"].value == "finish":
	lastFilename = filenames.pop()

	for filename in filenames:
		deleteFile(filename)

	cookie["filenames"] = ""
	print("Location: view.cgi?id="+str(1))
	print(cookie)
	print("\r\n\r\n")

elif arguments["action"].value == "undo":
	lastFilename = filenames.pop()
	deleteFile(lastFilename)
	cookie["filenames"] = ",".join(filenames)

	print("Location: edit.cgi")
	print(cookie)
	print("\r\n\r\n")

else:
	lastFilename = filenames[len(filenames)-1]
	path = os.path.dirname(os.path.realpath(__file__))+"/files/"+lastFilename
	command = "convert \""+path+"\" -bordercolor red -border 10 wow.jpg"
	print("Content-type: text/html")
	print(command)
	subprocess.call(command)
	filenames.append('wow.jpg')
	cookie["filenames"] = ",".join(filenames)
	print("Location: edit.cgi")
	print(cookie)
	print("\r\n\r\n")
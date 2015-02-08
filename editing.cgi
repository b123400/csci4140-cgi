#!/usr/bin/python

import cgi
import cgitb; cgitb.enable() # Optional; for debugging only

print ""

arguments = cgi.FieldStorage()
for i in arguments.keys():
	print arguments[i].value

if arguments["action"] == "discard"
	print("Location: /index.cgi\r\n\r\n")
else if arguments["action"] == "finish"
	print("Location: /view.cgi?id="+1+"\r\n\r\n")
else if arguments["action"] == "undo"
	print("Location: /edit.cgi")
else
	print("Location: /edit.cgi")
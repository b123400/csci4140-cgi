#!/usr/bin/python

import cgi
import cgitb; cgitb.enable() # Optional; for debugging only

arguments = cgi.FieldStorage()

if arguments["action"].value == "discard":
	print("Location: index.cgi\r\n\r\n")
elif arguments["action"].value == "finish":
	print("Location: view.cgi?id="+1+"\r\n\r\n")
elif arguments["action"].value == "undo":
	print("Location: edit.cgi\r\n\r\n")
else:
	print("Location: edit.cgi\r\n\r\n")
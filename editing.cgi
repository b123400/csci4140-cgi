#!/usr/bin/python

import cgi
import cgitb; cgitb.enable() # Optional; for debugging only

print ""

arguments = cgi.FieldStorage()

if arguments["action"] == "discard":
	print("Location: index.cgi\r\n\r\n")
elif arguments["action"] == "finish":
	print("Location: view.cgi?id="+1+"\r\n\r\n")
elif arguments["action"] == "undo":
	print("Location: edit.cgi")
else:
	print("Location: edit.cgi")
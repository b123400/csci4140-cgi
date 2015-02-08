#!/usr/bin/python

import cgi
import cgitb; cgitb.enable() # Optional; for debugging only

print ""

arguments = cgi.FieldStorage()

print("Content-type: text/html\r\n\r\n")

printf("""<img src="/files/%s" /> """ % arguments["image"].value)
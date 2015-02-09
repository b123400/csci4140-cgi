#!/usr/bin/python

import cgi
import cgitb; cgitb.enable() # Optional; for debugging only

arguments = cgi.FieldStorage()

print("Content-type: text/html\r\n\r\n")

print("""<img src="/finished/%s" /> """ % arguments["image"].value)

print("""<a href="/">back to index</a> """)
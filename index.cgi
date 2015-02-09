#!/usr/bin/python

print("Content-type: text/html\r\n\r\n")

import Cookie
import os
import cgi
import cgitb; cgitb.enable() # Optional; for debugging only
from os.path import isfile, join
import math

outpath = os.path.dirname(os.path.realpath(__file__))+"/finished/"
arguments = cgi.FieldStorage()
page = 0

if not os.path.exists(os.path.dirname(outpath)):
	os.makedirs(os.path.dirname(outpath))

cookie = Cookie.SimpleCookie()
canResume = False
try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	filenames = cookie["filenames"].value
	if len(filenames) > 0:
		canResume = True
except Exception, e:
	pass

try:
	page = int(arguments["page"].value)
except Exception, e:
	pass

print("""
	<html>
		<body style="text-align:center;">
		<div style="width: 800px; margin: auto;">
	""")

onlyfiles = [ f for f in os.listdir(outpath) if os.path.isfile(join(outpath,f)) ]
onlyfiles.sort(key=lambda x: os.path.getmtime(join(outpath,x)))
i = 0
for f in reversed(onlyfiles):
	if i >= 8*(page+1):
		break
	elif i >= 8*page:
		print("""
			<a href="/view.cgi?image=%s">
			<div style="float:left; width:200px; height:200px; background-image:url(/finished/%s); background-size:cover; display:inline-block;"></div>
			</a>""" % (f,f)
			)
	i += 1

print("""<div style="clear:both;"></div></div>""")

pageCount = math.ceil(len(onlyfiles) / 8.0)
if page > 0:
	print(""" <a href="/?page=%d">prev</a> | """ % (page-1))

print(""" page %d of %d """ %(page+1, pageCount))

if page < pageCount-1:
	print(""" | <a href="/?page=%d">next</a> """ % (page+1))

if canResume:
	print("""<BR/> ===================== <BR/><a href="/edit.cgi">resume</a> | """)

print("""
			<a href="/upload.html">upload</a>
		</body>
	</html>
	""")
#!/usr/bin/python

print("Content-type: text/html\r\n\r\n")

import Cookie
import os
import cgi
import cgitb; cgitb.enable() # Optional; for debugging only
from os.path import isfile, join

outpath = os.path.dirname(os.path.realpath(__file__))+"/files/"

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

print("""
	<html>
		<body>
	""")

onlyfiles = [ f for f in os.listdir(outpath) if os.path.isfile(join(outpath,f)) ]
onlyfiles.sort(key=lambda x: os.path.getmtime(x))
for f in onlyfiles:
	print("""
		<a href="/view.cgi?image=%s">
		<div style="width:200px; height:200px; background-image:url(/files/%s); background-size:cover; display:inline-block;"></div>
		</a>""" % (f,f)
		)

if canResume:
	print("""<a href="/edit.cgi">resume</a>""")

print("""
			<a href="/upload.html">upload</a>
		</body>
	</html>
	""")
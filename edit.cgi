#!/usr/bin/python

import Cookie
import os
import cgi
import cgitb; cgitb.enable() # Optional; for debugging only

cookie = Cookie.SimpleCookie()
lastFilename = ""
try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	filenames = cookie["filenames"].value
	filenames = filenames.split(",")
	lastFilename = filenames[len(filenames)-1]
except Exception, e:
	pass

print("Content-type: text/html\r\n\r\n")

print("""
	<html>
		<body>
		<table style="width:100%;">
			<tr>
				<td style="width:50%;">
	""")

print("""<img src="/files/%s" alt="" />""" % lastFilename)

print("""
	</td>
	<td>
		<form action="/editing.cgi" method="post">
		<input name="action" type="submit" value="border" />
		<input name="action" type="submit" value="lomo" />
		<input name="action" type="submit" value="lens flare" />
		<input name="action" type="submit" value="black white" />
		<input name="action" type="submit" value="blur" /> <BR/>
		=======================
		Message: <input type="text" name="message" /> <BR/>
		Font: <select name="font"><BR/>
			<option value="Times">Times</option>
			<option value="Courier">Courier</option>
			<option value="Helvetica">Helvetica</option>
		</select><BR/>
		Font size: <input name="fontsize" type="number" min="10" max="48" step="1" value="24" /><BR/>
		
		<input name="action" type="submit" value="annotate top" />
		<input name="action" type="submit" value="annotate bottom" /><BR/>
		===================== <BR/>
		<input name="action" type="submit" value="undo" />
		<input name="action" type="submit" value="discard" />
		<input name="action" type="submit" value="finish" />
		</form>
		</td>
	</body>
	</html>
	""")
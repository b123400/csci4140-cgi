#!/usr/bin/python

print("Content-type: text/html\r\n\r\n")

print("""
	<html>
		<body>
		
		<form action="/editing.cgi" method="post">
			edit page here
			<input name="action" type="submit" value="filter1" />
			<input name="action" type="submit" value="filter2" />
			<input name="action" type="submit" value="filter2" />

			<input name="action" type="submit" value="text top" />
			<input name="action" type="submit" value="text bottom" />

			<input name="action" type="submit" value="undo" />
			<input name="action" type="submit" value="discard" />
			<input name="action" type="submit" value="finish" />
		</form>
		</body>
	</html>
	""")
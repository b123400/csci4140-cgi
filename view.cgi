import cgi
import cgitb; cgitb.enable() # Optional; for debugging only

print ""

arguments = cgi.FieldStorage()

print("Content-type: text/html\r\n\r\n")

print("now viewing "+ arguments["id"])
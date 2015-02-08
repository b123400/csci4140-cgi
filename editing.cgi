#!/usr/bin/python

import Cookie
import os
import cgi
import cgitb; cgitb.enable() # Optional; for debugging only
import subprocess
import uuid

arguments = cgi.FieldStorage()

cookie = Cookie.SimpleCookie()
filenames = []
try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	filenames = cookie["filenames"].value
	filenames = filenames.split(",")
except Exception, e:
	pass

def deleteFile(filename):
	os.remove('files/'+filename)

if arguments["action"].value == "discard":

	for filename in filenames:
		deleteFile(filename)

	cookie["filenames"] = ""
	print("Location: index.cgi")
	print(cookie)
	print("\r\n\r\n")

elif arguments["action"].value == "finish":
	lastFilename = filenames.pop()

	for filename in filenames:
		deleteFile(filename)

	cookie["filenames"] = ""
	print("Location: view.cgi?id="+str(1))
	print(cookie)
	print("\r\n\r\n")

elif arguments["action"].value == "undo":
	lastFilename = filenames.pop()
	deleteFile(lastFilename)
	cookie["filenames"] = ",".join(filenames)

	print("Location: edit.cgi")
	print(cookie)
	print("\r\n\r\n")

else:
	lastFilename = filenames[len(filenames)-1]
	extension = lastFilename.split(".")[-1].lower()
	path = os.path.dirname(os.path.realpath(__file__))+"/files/"+lastFilename
	temppath = uuid.uuid4()+"."+extension
	outfilename = uuid.uuid4()+"."+extension
	outpath = "files/"+outfilename
	command = ""

	identifyCommand = "identify %s" % path
	p = subprocess.Popen(identifyCommand, shell=True, stdout=subprocess.PIPE)
	output = p.communicate()[0]
	width, height = output.split(" ")[2].split("x")

	if arguments["action"].value == "border":
		command = """
		convert "%s" -bordercolor red -border 10 "%s"
		""" % (path, outpath)

	elif arguments["action"].value == "lomo":
		command = """
		convert "%s" -channel R -level 33% -channel G -level 33% "%s"
		""" % (path, outpath)

	elif arguments["action"].value == "lens flare":
		command = """
		convert lensflare.png -resize %dx tmp.png;
		composite -compose screen -gravity northwest tmp.png "%s" "%s"
		""" % (width, path, outpath)

	elif arguments["action"].value == "black white":
		command = """
		convert "%s" -type grayscale "%s";
		convert bwgrad.png -resize %dx%d\! tmp.png;
		composite -compose softlight -gravity center tmp.png %s %s;
		""" % (path, temppath, width, height, temppath, outpath)

	elif arguments["action"].value == "blur":
		command = "convert %s -blur 0.5x2 %s" % (path, outpath)

	else:
		print("Content-type: text/html\r\n\r\n")
		print("unknow action"+arguments["action"].value)
		exit(0)

	# print("Content-type: text/html\r\n\r\n")
	# print(command)
	subprocess.call(command, shell=True)
	filenames.append(outfilename)
	cookie["filenames"] = ",".join(filenames)
	print("Location: edit.cgi")
	print(cookie)
	print("\r\n\r\n")
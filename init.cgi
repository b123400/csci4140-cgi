#!/usr/bin/python

import shutil

print("Content-type: text/html\r\n\r\n")

shutil.rmtree("./files",ignore_errors=True)
shutil.rmtree("./finished",ignore_errors=True)

print("""init done. <a href="/">go to index</a> """)
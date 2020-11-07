from sys import argv
from stml_funcs import *
file = argv[1]
try:
	head,body=open(file).read().replace(multicode,"\n").split(bsplit)#split head and body
	th=[i.split(comment)[0] for i in head.split(";")[1].split("\n")]#split title and head
	bct=[i.split(comment)[0] for i in body.split("\n")]#split body argument and content
	code=tag("html",tag("head",tag("title",th[0])+convert("\n".join(th[1:])))+tag("body",convert('\n'.join(bct[1:])),bct[0].lstrip()))
	print(code);c=True
except Exception as err:
	print("SyntaxError",err);c=False
try:
	if c:
		filename=file.split("\\")[-1]
		open(f"{filename.split('.')[0]}.html","w").write(code)#Saving html
except Exception as err:
	print("I\\O Error: Can't save",err)
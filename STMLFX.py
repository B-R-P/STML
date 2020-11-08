from sys import argv
from stml_funcs import *
fileaddr = argv[1]
try:
	file=open(fileaddr).read().replace(multicode,"\n")
	file=sub(rcomment,"",file)#Removing comment
	code=convert(file)
	print(code);c=True
except Exception as err:
	print("SyntaxError:",err);c=False
try:
	if c:
		filename=fileaddr.split("\\")[-1]
		open(f"{filename.split('.')[0]}.xml","w").write(code)#Saving xml
except Exception as err:
	print("I\\O Error: Can't save",err)
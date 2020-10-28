from sys import argv
file = argv[1]
dstart="<"
dend="/>"
lsymbol="- "
mline="-!"
nline="n|"
bsplit="B!"
singleton="$"
comment="/#"
def marg(tg,c):#Extract multiple arguments
	tg=tg.split(" ")
	if len(tg)==1:
		w=[""]
	else:
		w=''.join(tg[1:]).split("|")
	tsp=tg[0].split(",")
	w+=['']*(len(tsp)-len(w))
	for i,ar in zip(reversed(tsp[1:]),reversed(w[1:])):
		c=tag(i,c,ar)
	return tsp[0],c,w[0]
def tag(t,i="",a=""):# return <t a>i</t>
	if a!="":
		a=" "+a.replace("=",'="').replace(",",'" ')+'"'
	if singleton in t:
		return '<'+t.replace(singleton,"")+a+'>'+convert(i)
	return '<'+t+a+'>'+i+'</'+t+'>'
def inside(txt,s,e):#Extract string between s and e from txt
	c=0
	t=""
	blk=[]
	for i in range(len(txt)):
		st = txt[i:i+len(s)]
		if c==0:
			if t!="":
				blk.append(t[len(s):1-len(e)])
				t=""
			b=False
		if st==s:
			b=True
			c+=1
		et=txt[i:i+len(e)]
		if et==e and c>0:
			c-=1
		if b:
			t+=st[0]
	return blk
def ext(c):#For inline stml and to extract content
	if dstart in c and dend in c:
		cos=inside(c,dstart,dend)
		for co in cos:
			if singleton in co:
				ts=[co]
				sco=""
			else:
				ts=co.split(lsymbol)
				sco=lsymbol.join(ts[1:])
				if dstart in sco and dend in sco:
					sco=ext(lsymbol+sco)
				sco=sco.replace("  ","&nbsp;&nbsp;")
			c=c.replace(dstart+co+dend,tag(*marg(ts[0],sco)))
	c=c.split(lsymbol)[1]
	return c
def parse(blk):#To parse stml
	blk=blk.replace(nline,"<br>")
	if "\t" in blk:
		blk=[i.replace("\t","",1) for i in blk.split("\n")]
		tg=blk[0]
		c=convert('\n'.join(blk[1:]))
	else:
		ts=blk.rstrip("\n").split("\n")#Spliting tag and content
		tg=ts[0]
		c="".join([ext(i)for i in ts[1:]])#Calling ext
	return tag(*marg(tg,c))
def convert(file):#To convert stml to html
	code=""
	blk=""
	onblk=False
	ml=False
	for line in file.split("\n"):
		if line.strip()=="":
			continue
		if line[0] in ["\t"," "] or ml or not onblk:
			if line[:2]==mline:
				ml= not ml#Changing multiline mode
				line=line.replace(mline,lsymbol)
			elif ml:
				line=lsymbol+line
			elif line[0]==" ":
				line="-"+line
			blk+=line+"\n"
			onblk=True
		else:
			code+=parse(blk)
			blk=line+"\n"
			onblk=singleton==line[0]#False and (singleton or not)
	if onblk:
		code+=parse(blk)
	return code
try:
	head,body=open(file).read().split(bsplit)#split head and body
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

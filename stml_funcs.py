from re import findall,compile as comp
dstart="<"#Literals
dend="/>"
lsymbol="- "
mline="-!"
nline="n|"
bsplit="B!"
singleton="$"
emptysing="$$"
comment="/#"
temp="%$#"#for temporary use
singline="=> "
multicode=" &; "
escape="\\"
attr=comp(r"(?<==)[^,]*(?=,)|(?<==).+(?=$)")
def marg(tg,c,fl=""):#Extract multiple arguments
	tg=tg.split(" ")
	if len(tg)==1:
		w=[""]
	else:
		w=' '.join(tg[1:])
		if singline in w:
			w=w.split(singline)
			fl=convert(c)
			c=w[1];w=w[0]
		w=w.split("|")
	tsp=tg[0].split(",")
	w+=['']*(len(tsp)-len(w))
	for i,ar in zip(reversed(tsp),reversed(w)):
		c=tag(i,c,ar,fl)
	return c
def tag(t,i="",a="",fl=""):# return <t a>i</t>
	if a!="":
		a=a.replace(escape+",",temp)
		for arg in findall(attr,a):
			a=a.replace("="+arg,'="'+arg+'"')
		a=" "+a.replace('",','" ').replace(temp,",")
	if emptysing in t:
		t = t.replace(singleton,"")
		fl=convert(i);i=""
	if singleton in t:
		t = t.replace(singleton,"")
		fl=convert(i);i=""
	else:
		fl='</'+t+'>'+fl
		if t=="p":
			i = i.replace(temp,"<br>")
	i=i.replace(temp,"")
	return '<'+t+a+'>'+i.replace("  ","&nbsp;&nbsp;")+fl
def inside(txt,s,e):#Extract string between s and e from txt
	c=0
	t="";slen=len(s)
	blk=[];elen=len(e)
	for i in range(len(txt)):
		st = txt[i:i+slen]
		if c==0:
			if t!="":
				blk.append(t[len(s):1-len(e)])
				t=""
			b=False
		if st==s:
			b=True
			c+=1
		et=txt[i:i+elen]
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
			c=c.replace(dstart+co+dend,marg(ts[0],sco))
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
	return marg(tg,c)
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
				continue
			elif ml:
				line=lsymbol+line+temp
			elif line[0]==" ":
				line="-"+line
			blk+=line+"\n"
			onblk=True
		else:
			code+=parse(blk)
			blk=line+"\n"
			onblk=(singleton==line[0] or singline in line)#False and (singleton or not)
	if onblk:
		code+=parse(blk)
	return code

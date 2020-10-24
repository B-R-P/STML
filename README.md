# <u>**STML**</u>

#### Simple Text Markup Language

**STML** is **simplified** version of HTML

It is more **cleaner** than html and increase your coding **speed**. 

#### In HTML

``` html
<html>
	<head>
		<title>Hello World</title><!--Comment-->
        <meta name="STML Site">
	</head>
	<body style="background-color:black;">
		<font color="white" size="5">
			<h1>
				<u>
                    <center>Heading 1</center>
                </u>
			</h1>
			<h2>
				<i>Heading 2</i>
			</h2>
			<h3>
				<s>Heading 3</s>
			</h3>
			<p>
                This is first line in <b style="color:red">paragraph</b><br>
                This is middle line in <i style="color:green">paragraph</i><br>
                This is last line in <u style="color:blue;">paragraph</u>
			</p>
		</font>
	</body>
</html>
```

#### In STML

```STML
;Hello World/#Comment
$meta name=STML site
B!style=background-color:black;
font color=white,size=5
	h1,u,center
	 Heading 1
	h2,i
	 Heading 2
	h3,s
	 Heading 3
	p
	-!This is first line in <b style=color:red- paragraph/>n|
	This is middle line in <i style=color:green- paragraph/>n|
	-!This is last line in <u style=color:blue;- paragraph/>
```

#### Usage

```bash
py stml.py filename.stml
```

HTML file will be saved as filename.html
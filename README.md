# <u>**STML**</u>

#### Simple Text Markup Language

Source-to-Source Compiler

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
For *Windows*

Download [stml.zip](https://drive.google.com/uc?export=download&id=1F_dwS92XnjJnBcbYYbkn5_W2z-3ky1mX) and extract stml folder.Add stml folder to PATHS in environmental variable.

```cmd
stml filname.stml
```
For Sublime Text Editor

[Build System](https://drive.google.com/uc?export=download&id=1wyzE7zZXEFoTzgcyTqkB3Un7_6VFoCOS)

[Syntax](https://gdurl.com/z1Cp/download)
(*Not Perfect*)

HTML file will be saved as filename.html

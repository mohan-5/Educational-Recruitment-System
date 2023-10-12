#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql

mydb=pymysql.Connect(host="localhost",user="root",password="mohan",database="first_project")
mycursor=mydb.cursor()

data=cgi.FieldStorage()
value=0

a=data.getvalue("o1")
b=data.getvalue("o2")
c=data.getvalue("o3")
d=data.getvalue("o4")
e=data.getvalue("o5")
f=data.getvalue("o6")
g=data.getvalue("o7")
h=data.getvalue("o8")
i=data.getvalue("o9")
j=data.getvalue("o10")


if a=="Object class":
    value+=1
else:
    value+=0
if b=="4":
    value+=1
else:
    value+=0
if c=="JVM":
    value+=1
else:
    value+=0
if d=="java.lang":
    value+=1
else:
    value+=0
if e=="run() method is used to begin execution of a thread before start() method in special cases":
    value+=1
else:
    value+=0
if f=="try":
    value+=1
else:
    value+=0
if g=="Void":
    value+=1
else:
    value+=0
if h=="0 to 65535":
    value+=1
else:
    value+=0
if i=="ServerSocket":
    value+=1
else:
    value+=0
if j=="Servlets execute within the address space of web server, platform independent and uses the functionality of java class libraries":
    value+=1
else:
    value+=0

query="insert into java_final_quiz values(%s)"
values=[value]
mycursor.execute(query,values)
mydb.commit()

print('''
<style>
            body{
                    background-image:url('final.jpg');
                    background-repeat:no-repeat;
                    background-size:cover;
                    background-position: center;
                    height: 100vh;
            }
            </style>
            <!DOCTYPE html>
            <html>
            <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
            .navbar{
                    width: 1200px;
                    height:75px;
                    margin: auto;
            }

            .icon{
                    width: 200px;
                    float: left;
                    height: 70px;
            }

            .logo{
                    color: #ff7200;
                    font-size: 65px;
                    font-family: Arial;
                    padding-left: 20px;
                    float: left;
                    padding-top: 0px;
            }
            .menu{
                    width: 400px;
                    float: left;
                    height: 70px;
            }

            ul{
                    float: left;
                    display: flex;
                    justify-content: center;
                    align-items: center;
            }

            ul li{
                    list-style: none;
                    margin-left: 55px;
                    margin-top: 50px;
                    font-size: 25px;
            }

            ul li a{
                    text-decoration: none;
                    color: black;
                    font-family: Arial;
                    font-weight: bold;
                    transition: 0.4s ease-in-out;
            }

            ul li a:hover{
                    color: #ff7200;
            }

            .content{
                    width: 1200px;
                    height: auto;
                    margin: auto;
                    color: black;
                    position: relative;
                    font-size: 20px;
            }

            .block {
              width: 11%;
              height: 8%;
            padding: 5px 15px;
            cursor: pointer;
            display: block;
            margin: auto;
            background: linear-gradient(to right, #ff105f,#ffad06);
            border: 0;
            outline: none;
            border-radius: 30px;
            }

            .block:hover {
              background-color: #ddd;
              color: black;
            }
            
            </style>
            
            </head>
            
            <body>
            <div class="navbar">
			<div class="icon">
				<h1 class="logo">MHN</h1>
			</div>
			<div class="menu">
				<ul>
					<li><a href="#">HOME</a></li>
					<li><a href="#">ABOUT</a></li>
					<li><a href="#">SERVICE</a></li>
					<li><a href="#">COURSE</a></li>
					<li><a href="#">CONTACT</a></li>
				</ul>
			</div>			
    	    </div>
	    <br><br><hr>
	    <div class="content">
			<br><br><h1><center>You have sucessfully completed our course and assessment <br><br><br>The Recruitor will reach you soon.</center></h1><br>
	    </div>
	    <br><br><center><a href='index.html'<button class="block"><center><h2><ins>Logout</ins></h2></center></button></center></a>
            </body>
            </html>
''')

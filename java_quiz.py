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


if a=="James Gosling":
    value+=1
else:
    value+=0
if b=="Java is a platform-independent programming language":
    value+=1
else:
    value+=0
if c=="JDK":
    value+=1
else:
    value+=0
if d=="Use of pointers":
    value+=1
else:
    value+=0
if e=="keyword":
    value+=1
else:
    value+=0
if f==".java":
    value+=1
else:
    value+=0
if g=="JAVA_HOME":
    value+=1
else:
    value+=0
if h=="Compile time polymorphism":
    value+=1
else:
    value+=0
if i=="Floating-point value assigned to an integer type":
    value+=1
else:
    value+=0
if j==".class":
    value+=1
else:
    value+=0

query="insert into java_quizz values(%s)"
values=[value]
mycursor.execute(query,values)
mydb.commit()

print('''
<style>
            body{
                    background-image:url('img2.jpg');
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
                    color: #fff;
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
                    color: #fff;
                    position: relative;
                    font-size: 30px;
            }

            .block {
              display: block;
              width: 350px;
              height: 50px;               
              border-radius: 30px;
              background-color: #FF8C00	;
              color: white;
              padding: 10px 20px;
              font-size: 14px;
              cursor: pointer;
              text-align: center;
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
			<h1><center><ins>Congratulation..!</ins> <br>you are eligible for our Online Course</center></h1><br>
	    </div>
	    <br><br><center><a href='java_course.html'<button class="block"><center><h2><ins>Click Here to Start Online Course</ins></h2></center></button></center></a>
            </body>
            </html>
''')

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


if a=="12":
    value+=1
else:
    value+=0
if b=="True":
    value+=1
else:
    value+=0
if c=="getopt":
    value+=1
else:
    value+=0
if d=="A[1][2]":
    value+=1
else:
    value+=0
if e=="-":
    value+=1
else:
    value+=0
if f=="Abc. def":
    value+=1
else:
    value+=0
if g=="set()":
    value+=1
else:
    value+=0
if h=="[1, 3, 5, 7, 8]":
    value+=1
else:
    value+=0
if i=="list1.append(5)":
    value+=1
else:
    value+=0
if j=="[4, 3]":
    value+=1
else:
    value+=0

if value>=7:
    result="Eligible"
else:
    result="Not Eligible"

mycursor.execute("select * from member_details")
name=mycursor.fetchall()

for i in name:
    uname=i[0]

query="insert into final_quiz values(%s,%s,%s)"
values=[value,uname,result]
mycursor.execute(query,values)
mydb.commit()

mycursor.execute("select * from final_quiz")
var=mycursor.fetchall()

for i in var:
    mar=i[0]



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
            <html lang="en">
            <head>
            <title>Webpage Design</title>
            <link rel="stylesheet" href="python_student_final.css">
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
	    </body>
            </html>

            ''')

print('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <title>Webpage Design</title>
            <link rel="stylesheet" href="python_student_final.css">
            </head>
            <body>

	    <div class="content">
			<br><br><h1><center>You have sucessfully completed our course and assessment<br></center></h1><br><br>
	    </div>
	    </body>
	    </html>
	    ''')
print("<div class=""content""><center><h1><ins>Your Total Marks Scored out of 10 is: </ins>",mar,"</h1></center></div>")

print('''

<!DOCTYPE html>
            <html lang="en">
            <head>
            <title>Webpage Design</title>
            <link rel="stylesheet" href="python_student_final.css">
            </head>
            <body>
            <div class="content">
			<br><br><h1><center>The Recruitor will reach you soon.</center></h1><br>
	    </div>
	    <br><br><center><a href='index.html'<button class="block"><center><h2><ins>Logout</ins></h2></center></button></center></a>
            </body>
            </html>
''')



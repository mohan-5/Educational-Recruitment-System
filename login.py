#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql

mydb=pymysql.Connect(host="localhost",user="root",password="mohan",database="first_project")
cur=mydb.cursor()

data=cgi.FieldStorage()
logmail=data.getvalue("loginmail")
logpass=data.getvalue("loginpswd")

cur.execute("select * from member_details")
var=cur.fetchall()

for i in var:    
    if i[1]==logmail and i[2]==logpass:
            print('''
            <style>
            body{
                    background-image:url('img.jpg');
                    background-repeat:no-repeat;
                    background-size:cover;
            }
            </style>
            <!DOCTYPE html>
            <html>
            <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
            .navbar{
                    width: 1200px;
                    height:50px;
                    margin: auto;
            }

            .icon{
                    width: 200px;
                    float: left;
                    height: 40px;
            }

            .logo{
                    color: #ff7200;
                    font-size: 65px;
                    font-family: Arial;
                    padding-left: 20px;
                    float: left;
                    padding-top: -20px;
            }
            .menu{
                    width: 400px;
                    float: left;
                    height: 50px;
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
                    margin-top: 30px;
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
            
            .block{
                position: relative;
                width: 500px;
                height: 200px;
                top: -30px;
                background: transparent;
                border: 2px solid rgba(255, 255, 255, .5);
                border-radius: 30px;
                backdrop-filter: blur(20px);
                box-shadow: 0 0 30px rgba(0, 0, 0, .5);
                color: black;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .block:hover {
              background-color: #F67E64;
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
            <br><br><br><center><a href='python_open_quizz.html'<button class="block"><center><h2><ins>Cognizent wants Python Developers</ins></h2></center><br><center><h4><i>did you want to grap the oppurtunity..</i></h4></center><h4><center>Click this button</center></h4></button></center></a>
            <br><br><center><a href='java_open_quizz.html'<button class="block"><center><h2><ins>TCS wants Java Developers</ins></h2></center><center><h4><i>did you want to grap the oppurtunity..</i></h4></center><h4><center>Click this button</center><h4></button></center></a>
            </body>
            </html>
        
            ''')    
    else:
        print('''
            <style>
            body{
                    background-image:url('oops.jpg');
                    background-repeat:no-repeat;
                    background-size:cover;
            }
            </style>
        
        ''')
        print("<br><br><br><br><label style=""font-size:30px"";><center><h1> incorrect login/ password</h1></center></label>")  
cur.execute("select * from recruitor_details")
rec=cur.fetchall()

for i in rec:    
    if i[1]==logmail and i[2]==logpass:
        

        print('''
        <style>
        body{
                background-image:url('final.jpg');
                background-repeat:no-repeat;
                background-size:cover;
                    
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
			    <br><h1 class="logo">MHN</h1>
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
		    <br><h1 style="font-size:40px;color:red"><center><ins>Detail of student who finished the course</ins></center></h1>
		    <hr><br>
	</div>
	</body>
	</html>
	''')
        cur.execute("select * from member_details")
        var=cur.fetchall()

        for i in var:
            cur.execute("SELECT user_name FROM member_details")
            var=cur.fetchall()
            student_name=i[0]
            student_mail=i[1]
            student_mobile=i[3]

        cur.execute("select * from quizz")
        var=cur.fetchall()

        for i in var:
            python_open_quiz_mark=i[0]

        cur.execute("select * from final_quiz")
        var=cur.fetchall()

        for i in var:
            python_final_quiz_mark=i[0]

        cur.execute("select * from java_quizz")
        var=cur.fetchall()

        for i in var:
            java_open_quiz_mark=i[0]

        cur.execute("select * from final_quiz")
        var=cur.fetchall()

        for i in var:
            java_final_quiz_mark=i[0]
            status=i[2]
        print('''

        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Webpage Design</title>
        <link rel="stylesheet" href="python_student_final.css">
        <style>
        th,td{
	border:1px solid black;
	border-collapse:collapse;
	background-color:pink;
	border-radius:10px;
	border-style:ridge;
	border-color:blue;
	padding:15px;
	border-spacing:40px;
        }
        tr:nth-child(even){
	background-color:blue;
        }
        </style>
        </head>
        <body>
        <table style="width:100%">
	<caption style="font-size:40px;color:blue"><center><ins><b>Student Details</b></ins></center></caption>
	<tr style="height:50px">
		<th style="width:15%;height:50%">Student Name</th>
		<th style="width:10%">Student Mail Id</th>
		<th style="width:15%">Student Mobile Number</th>
		<th style="width:15%">Student Entrance Quiz Score</th>
		<th style="width:15%">Student Final Quiz Score</th>
		<th style="width:15%">Eligibility Status</th>
	</tr>
	<tr>''')
        print("<td><center>",student_name,"</center></td>")
        print("<td><center>",student_mail,"</center></td>")
        print("<td><center>",student_mobile,"</center></td>")
        print("<td><center>",python_open_quiz_mark,"</center></td>")
        print("<td><center>",python_final_quiz_mark,"</center></td>")
        print("<td><b><center>",status,"</center></b></td>")
        print('''
        </tr>
        </table>
        
	<br><br><br><br><br><br><br><br><br><center><a href='index.html'<button class="block"><center><h2><ins>Logout</ins></h2></center></button></center></a>
        </body>
        </html>
        ''')
    else:
        print('''
            <style>
            body{
                    background-image:url('oops.jpg');
                    background-repeat:no-repeat;
                    background-size:cover;
            }
            </style>
        
        ''')
        print("<br><br><br><br><label style=""font-size:30px"";><center><h1> incorrect login/ password</h1></center></label>")
            

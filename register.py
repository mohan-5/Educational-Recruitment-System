#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql

mydb=pymysql.Connect(host="localhost",user="root",password="mohan",database="first_project")
mycursor=mydb.cursor()

data=cgi.FieldStorage()
name=data.getvalue("name")
mail=data.getvalue("mail")
pswd=data.getvalue("pass")
mbl=data.getvalue("mobile")
idnty=data.getvalue("id")

if idnty=="Student":

    query="insert into member_details values(%s,%s,%s,%s)"
    values=[name,mail,pswd,mbl]
    mycursor.execute(query,values)
    mydb.commit()

elif idnty=="Recruitor":
    query="insert into recruitor_details values(%s,%s,%s,%s)"
    values=[name,mail,pswd,mbl]
    mycursor.execute(query,values)
    mydb.commit()

print('''
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Webpage Design</title>
	<link rel="stylesheet" href="style.css">
</head>
<body>
	<div class="main">
		<div class="navbar">
			<div class="icon">
				<h1 class="logo">MHN<h1>
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
		<div class="content">
			<h1>Course & <br>Job<br>Portal</h1>
			<br><p class="par">MHN is a platform that allows instructors to build online courses on their preferred topics.<br><br>Using MHN's course development 					tools, instructors can upload videos,<br><br> source code for developers, and any other content that learners might find helpful.</p>
				<div class="form">
					<div class="button-box">
						<div id="btn"></div>
						<button type="button" class="toggle-btn" onclick="login()">Log In</button>
						<button type="button" class="toggle-btn" onclick="register()">Register</button>
					</div>
					<form action=login.py id="login" class="input-group" method="post">
						<input type="email" class="input-field" name="loginmail" placeholder="Email Id" required>
						<input type="password" class="input-field" name="loginpswd" placeholder="Enter password" required>
						<input type="checkbox" class="check-box"><span>Remember Password</span>
						<button type="submit" class="submit-btn">Log in</button>
					</form>
					
					<form action=register.py id="register" class="input-group" method="post">
						<input type="text" class="input-field" name="name" placeholder="User Name" required>
						<input type="email" class="input-field" name="mail" placeholder="Email Id" required>
						<input type="password" class="input-field" name="pass" placeholder="Enter password" required>
						<input type="phone" class="input-field" name="mobile" placeholder="Enter mobile number" required><br><br>
						<label><b>You are:</b></label>&emsp;&emsp;<input type ="radio" name="id" value="Student">&emsp;Student&emsp;
						<input type ="radio" name="id" value="Recruitor">&emsp;Recruitor</center><br>						
						<input type="checkbox" class="check-box"><span>I agree to the terms & conditions</span>
						<button type="submit" class="submit-btn" onclick="alert('You have successfully signup')">Register</button>

					</form>
					</div>
				</div>
		</div>
	</div>
<script>
var x= document.getElementById("login");
var y= document.getElementById("register");
var z= document.getElementById("btn");

function register(){
	x.style.left="-400px";
	y.style.left= "50px";
	z.style.left= "110px";
}

function login(){
	x.style.left="50px";
	y.style.left= "450px";
	z.style.left= "0";
}

</script>
</body>
</html>
''')

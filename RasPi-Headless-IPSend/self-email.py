import smtplib
import ssl
from urllib.request import urlopen

#dont name this file "email.py or else it will conflict with imported libraries"

my_ip = urlopen('http://ip.42.pl/raw').read()
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
#need to enable "less secure app access" on your google account.
email_file = open("email.txt")
password_file = open("password.txt")
email = email_file.readline()
password = password_file.readline()
message = my_ip

with smtplib.SMTP_SSL(smtp_server, port) as server:
    server.login(email, password)
    server.sendmail(email, email, message)


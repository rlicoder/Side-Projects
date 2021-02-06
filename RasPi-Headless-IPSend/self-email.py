import smtplib
import ssl

#dont name this file "email.py or else it will conflict with imported libraries"

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
#need to enable "less secure app access" on your google account.
email = input("Email: ");
password = input("Type your password and press enter: ")
message = "test"

with smtplib.SMTP_SSL(smtp_server, port) as server:
    server.login(email, password)
    server.sendmail(email, email, message)


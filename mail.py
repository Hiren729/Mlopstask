import smtplib, ssl

port = 465   #For SSL
smtp_server = "smtp.gmail.com"
sender_email = "hkruprela@gmail.com"  # Enter your address
password = 'hiruharshit' # Enter password
receiver_email = "hirenruprela@gmail.com"  # Enter receiver address

if accuracy > 99:
    message = """\
Subject:  Model successfully trained
Congratulations accuracy achieved."""
    
else:
    message = """\
Subject: Accuracy not met 
Accuracy not met, Training Again!"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
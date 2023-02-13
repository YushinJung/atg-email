import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_simpleNotice(sender_email, password, receiver_email, subject, text_message):
    smtp_server = 'smtp.gmail.com'
    port = 587
    
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email  
    
    part = MIMEText(text_message, 'plain')
    message.attach(part)
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
    except Exception as e:
        print(e)
        
import smtplib, ssl, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

def send_simpleEmail(sender_email, password, receiver_email, subject, text_message, d_file=''):
    if d_file == '':
        send_simpleNotice(sender_email, password, receiver_email, subject, text_message)
    else:
        send_email_wFile(sender_email, password, receiver_email, subject, text_message, d_file)
        
def send_simpleNotice(sender_email, password, receiver_email, subject, text_message):
    simple_email = SIMPLE_EMAIL()
    simple_email.set_sender(sender_email, password)
    simple_email.set_receiver(receiver_email)
    simple_email.add_title(subject)
    simple_email.add_message(text_message)
    simple_email.print_message()
    simple_email.send_email()
    
def send_email_wFile(sender_email, password, receiver_email, subject, text_message, d_file):
    simple_email = SIMPLE_EMAIL()
    simple_email.set_sender(sender_email, password)
    simple_email.set_receiver(receiver_email)
    simple_email.add_title(subject)
    simple_email.add_message(text_message)
    simple_email.add_file(d_file)
    simple_email.print_message()
    simple_email.send_email()
    
class SIMPLE_EMAIL:
    def __init__(self, smtp_server='smtp.gmail.com', port=587):
        self.smtp_server = smtp_server
        self.port = port
        self.message = MIMEMultipart()
        
    def set_sender(self, sender_email, password):
        self.sender_email = sender_email
        self.password = password
        
    def set_receiver(self, receiver_email):
        self.receiver_email = receiver_email

    def init_message(self):
        message = MIMEMultipart()
        self.message = message
        
    def add_title(self, subject):
        self.message['Subject'] = subject
        self.message['From'] = self.sender_email
        self.message['To'] = self.receiver_email
        
    def add_message(self, text_message):
        self.message.attach(MIMEText(text_message + '\n', 'plain'))
    
    def add_file(self, d_file):
        # https://stackoverflow.com/questions/3362600/how-to-send-email-attachments
        if not os.path.isfile(d_file):
            print(f'{Path(d_file).name} does not exist')
            self.add_message(f'{Path(d_file).name} does not exist' + '\n')
            return False
        part = MIMEBase('application', "octet-stream")
        with open(d_file, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={Path(d_file).name}')
        self.message.attach(part)
        return True
    
    def send_email(self):
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls(context=context)
                server.login(self.sender_email, self.password)
                server.sendmail(
                    self.sender_email, self.receiver_email, self.message.as_string()
                )
        except Exception as e:
            print(e)
    
    def print_message(self):
        print(self.message)
        return self.message  
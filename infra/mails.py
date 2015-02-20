import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Message(MIMEMultipart):
    def __init__(self):
        MIMEMultipart.__init__(self)

    def add_content(self, body):
        self.attach(MIMEText(body, 'plain','utf-8'))

class Messenger:
    def __init__(self, server, port, username, password):
        self.server = smtplib.SMTP('%s:%s'%(server, port))
        self.server.starttls()
        self.server.login(username, password)

    def __del__(self):
        self.server.quit()

    def send(self, send, recv, message):
        self.server.sendmail(send, recv, message.as_string())

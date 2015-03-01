import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import mail_config

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


need_to_send = []
smtp_server = Messenger(
    mail_config['smtp_server'],
    mail_config['smtp_port'],
    mail_config['username'],
    mail_config['password']
    )

def send_mail():
    message = Message()
    message['Subject'] = 'Crawler Notification Mail at %s'%(datetime.date.today())
    message['From'] = mail_config['from']
    message['To'] = mail_config['to']
    mail_body = '\n\n'.join(map(str, need_to_send))
    message.add_content(mail_body)

    smtp_server.send(
        mail_config['from'],
        mail_config['to'],
        message)

    del need_to_send[:]

#test code
if __name__ == '__main__':
    need_to_send.append('test content')
    need_to_send.append('test content2')
    send_mail()


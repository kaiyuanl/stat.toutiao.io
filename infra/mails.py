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

if __name__ == '__main__':
    server = 'smtp.tju.edu.cn'
    port = '25'
    username = 'kaiyuanl@tju.edu.cn'
    password = 'T%nt0wn'

    send = 'kaiyuanl@tju.edu.cn'
    recv = 'kaiyuanl@tju.edu.cn'

    body = '''test is a test mail'''

    message = Message()
    message['Subject'] = 'test mail'
    message['From'] = send
    message['To'] = recv
    message.add_content(body)

    smtp = Messenger(server, port, username, password)

    smtp.send(send, recv, message)

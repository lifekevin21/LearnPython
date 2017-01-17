# -*- coding:utf-8 -*-


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart, MIMEBase


import  smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'lifekevin21@126.com'
password = 'life901106ntes'
to_addr = 'lifekevin21@gmail.com'
smtp_server = 'smtp.126.com'


msg = MIMEMultipart()
msg['From'] = _format_addr('PythonTest <%s>' % from_addr)
msg['To'] = _format_addr('Admin <%s>' % to_addr)
msg['Subject'] = Header('Hello from SMTP...', 'utf-8').encode()

msg.attach(MIMEText('Send with file...', 'plain', 'utf-8'))

with open('E:/pic/test.jpg', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='test.jpg')

    mime.add_header('Content-Disposition', 'attachment', filename='test.hpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-ID', '<0>')

    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
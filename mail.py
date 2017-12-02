import smtplib

from email.mime.text import MIMEText
from config import me, pwd, to1, to2, cc1, cc2, out

txt = './mail.txt'

with open(txt, 'r') as fp:
    msg = MIMEText(fp.read())

server = smtplib.SMTP_SSL(out)
server.set_debuglevel(1)
server.login(me, pwd)

sender = me
recipient = [to1, to2]
cc = [cc1, cc2]
msg['Subject'] = 'Hourly Report 12/2/2017 1:00 PM'
msg['From'] = me
msg['To'] = ", ".join(recipient)
msg['CC'] = ", ".join(cc)
server.sendmail(me, me, msg.as_string())
server.quit()
print('done')

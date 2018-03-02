from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

smtp_server = 'XXXXXX' # smtp server of your email, such as 'smtp.sjtu.edu.cn' for SJTUer
from_addr = 'XXXXXX'   # your email address
password = 'XXXXXX'    # your email password
to_addr = 'XXXXXX'     # receiver address


def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def send(subject, text):
    msg = MIMEText(text, 'plain', 'gbk')
    msg['from'] = format_addr('Henry\'s VPS <%s>' % from_addr)
    msg['to'] = format_addr('Henry <%s>' % to_addr)
    msg['Subject']= Header(subject, 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25) # SMTP default port is 25
    server.set_debuglevel(0)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


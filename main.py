import update
import time
import re
import urllib2
import sendmail

url = 'http://www.jwc.sjtu.edu.cn/rss/rss_notice.aspx?SubjectID=198015&TemplateID=221009'
html = urllib2.urlopen(url).read()

links = re.findall('<link>(.*?)</link>', html)

with open('cache.txt', 'w') as cache:
    cache.write(links[2])

while True:
    new_msg_cnt, new_msg = update.update()
    if new_msg_cnt != 0:
        # print new_msg.decode('gbk')
        sendmail.send(('%d new messages published' % new_msg_cnt), new_msg)

    time.sleep(600)

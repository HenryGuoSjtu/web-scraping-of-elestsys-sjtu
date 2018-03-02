import re
import urllib2

url = 'http://www.jwc.sjtu.edu.cn/rss/rss_notice.aspx?SubjectID=198015&TemplateID=221009'


def update():
    with open('cache.txt', 'r') as cache:
        previous_link = cache.readline().strip()

    html = urllib2.urlopen(url).read()
    links = re.findall('<link>(.*?)</link>', html)

    new_msg_cnt = 0
    text = ''

    if links[1] != previous_link:
        titles = re.findall('<title>(.*?)</title>', html)
        dates = re.findall('<pubDate>(.*?)</pubDate>', html)
        for i in range(1, len(links)):
            if links[i] != previous_link:
                text = text + dates[i - 1] + '\n' + titles[i] + '\n' + links[i] + '\n\n'
                new_msg_cnt = new_msg_cnt + 1
            else:
                break

        with open('cache.txt', 'w') as cache:
            cache.write(links[1])

    return new_msg_cnt, text

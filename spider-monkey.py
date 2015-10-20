import urlparse
import urllib
import time
from bs4 import BeautifulSoup

#
# Site Mapper
#
#

url = "http://brentonwadehand.com"

urls = [url]
history = [url]

while urls != []:
    try:
        html = urllib.urlopen(urls[0]).read()
    except:
        print("Error" + url[0])

    soup = BeautifulSoup(html)

    urls.pop(0)

    for tag in soup.findAll('a', href=True):
        tag = urlparse.urljoin(url,tag['href'])

        if url in tag and tag not in history:
            urls.append(tag)
            history.append(tag)

    time.sleep(5)

print(history)



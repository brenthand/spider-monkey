import urlparse
import urllib
import time
from bs4 import BeautifulSoup
import sys

#
# Site Mapper
#
#

if len(sys.argv) < 2:
    print("Too few arguments")
    print("Usage: python spider-monkey.py http://example.com")
    exit(0)


index_list = []

url = sys.argv[1] # "http://brentonwadehand.com"

urls = [url]
history = [url]

while urls != []:
    try:
        html = urllib.urlopen(urls[0]).read()
    except:
        print("Error" + url[0])

    soup = BeautifulSoup(html)
    index_list.append(urls[0])
    urls.pop(0)

    for tag in soup.findAll('a', href=True):
        tag = urlparse.urljoin(url,tag['href'])

        if url in tag and tag not in history:
            urls.append(tag)
            history.append(tag)

    time.sleep(1)

#print(index_list)

index_html = "<html><body><ol>"
for url in index_list:
     index_html += "<li><a href='" + url + "' target=_'blank'>" + url + "<a/></li>"

index_html += "</ol></body></html>"

#Need to add argument for filename
with open(index_list.html, "w") as f:
    f.write(index.html)



import urllib.request, sys, time
from bs4 import BeautifulSoup
import requests
import pandas as pd

pagesToGet = 1

upperframe = []
for page in range(1, pagesToGet + 1):
    print('processing page :', page)
    url = 'https://www.newsnow.co.uk/h/Business+&+Finance?type=ln'
    print(url)

    # an exception might be thrown, so the code should be in a try-except block
    try:
        # use the browser to get the url. This is suspicious command that might blow up.
        page = requests.get(url)  # this might throw an exception if something goes wrong.

    except Exception as e:  # this describes what to do if an exception is thrown
        error_type, error_obj, error_info = sys.exc_info()  # get the exception information
        print('ERROR FOR LINK:', url)  # print the link that cause the problem
        print(error_type, 'Line:', error_info.tb_lineno)  # print error info and line that threw the exception
        continue  # ignore this page. Abandon this and go back.
    time.sleep(2)
    soup = BeautifulSoup(page.text, 'html.parser')
    frame = []
    links = soup.find_all('div', attrs={'rs-time-slot js-time-slot--server'})
    #div rs-time-slot js-time-slot--server
    print('tipo   ',type(links))
    print(len(links))
    filename = "NEWS.csv"
    f = open(filename, "w", encoding='utf-8')
    headers = "Statement,Link,Date, Source, Label\n"
    f.write(headers)
    Statement=""
    Link=""
    Source=""
    Label=""
    Date=""


    for j in links:
        print(j.get_text())
        print(j.get('href'))
        #soup.find_all('hl__inner'):
        # print('tipo ',type(j),'  informacion  ',j)
        # #print(tag.findChild("j")['title'])
        #for j in soup.find_all('hl__inner'):
        #    print(j.get('href'),' noticia   ',j.get_text())

        frame.append((Statement, Link, Date, Source, Label))
        f.write(Statement.replace(",", "^") + "," + Link + "," + Date.replace(",", "^") + "," + Source.replace(",",
                                                                                                               "^") + "," + Label.replace(
            ",", "^") + "\n")
    upperframe.extend(frame)
f.close()
data = pd.DataFrame(upperframe, columns=['Statement', 'Link', 'Date', 'Source', 'Label'])
data.head()
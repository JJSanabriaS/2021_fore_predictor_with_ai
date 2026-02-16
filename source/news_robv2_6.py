#influences Canada	USD/CAD	WTI crude oil and metals
#https://fxssi.com/high-impact-forex-news
#FxSSXI inificator
#Important Meetings: FOMC, ECB, BoE RBA, BoJ
#How often: Monthly

import urllib.request, sys, time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import pyttsx3
import os
import json
import datetime
def readn(nstr):
    engine = pyttsx3.init()
    engine.setProperty('voice', "english+f5")
    engine.setProperty('rate', 150)
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
    engine.say(nstr)
    engine.runAndWait()
    engine.stop()

def remove(string):
    pattern = re.compile(r'\n+')
    return re.sub(pattern, '', string)

pagesToGet = 1
upperframe = []
for page in range(1, pagesToGet + 1):
    print('processing page :', page)
    url = 'https://www.fxstreet.com'
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
    links = soup.find_all('h3', attrs={'fxs_entryHeadline'})
    print('tipo   ',type(links))
    print(len(links))
    filename = "NEWS.csv"
    f = open(filename, "w", encoding='utf-8')
    headers = "Statement,Link,Date, Source, Label\n"
    f.write(headers)
    Statement=""
    Link=""
    Date=""
    Source=""
    Label=""

    for j in links:
        for link in j.find_all('a'):
            #print('link extraido   ', link.get('href'))
            print(j.get_text(),' ref web  ',link.get('href'))
            #print(len(j.get_text()))
            readn(j.get_text())
    upperframe.extend(frame)
f.close()
data = pd.DataFrame(upperframe, columns=['Statement', 'Link', 'Date', 'Source', 'Label'])
data.head()
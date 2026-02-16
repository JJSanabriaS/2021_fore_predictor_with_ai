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
    links = soup.find_all('div', attrs={'newsfeed'})
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

    ol=0
    for j in links:
        print('contador  ',ol)
        #print((j))
        print(' teste salida www.newsnow.co.uk ')
        print(j.get_text(),'    fghrr ',len(j.get_text()))
        maxx = str(j.findAll("a", {"class": "hll"}))
        #print("  ", type(maxx),'longitud  ',len(maxx))
        #print(" ",type(j.get_text()))
        #print(' long   ',len(maxx),' tipo  ', type(maxx) )
        #print(maxx)
        ind=0
        ma=[]
        while (ind < len(maxx)):
            if 'href' in maxx:
              #match = re.findall(r'\*([^\*]*)\*=', maxx)
              #print('split  ',maxx.index("https"))
          #    print('cadena entrada   ',maxx)
              maxx1=maxx[maxx.index("https"):]
         #     print(maxx1)
              #print('split  ',maxx.index("https"),'  split2  ', maxx1.index("rel"),'    primera subcadena ',maxx1[0:maxx1.index("rel")-2])
              maxet=maxx1[0:maxx1.index("rel") - 2]
              maxx1=maxx1[maxx1.index("rel")-2:]
              ind=maxx1.index("rel")
              #print('cadena cortada  ',maxx1)
              ma.append(maxet)
              #print("pivot   ",ind)
              maxx=maxx1
            else:
              break
           #input("Press Enter to continue...")
           #print(maxx1[-5:])
           #</a>]


        print(ma)
        #find_all = lambda c, s: [x for x in range(c.find(s), len(c)) if c[x] == s]
        #find_all(sahref,'href=')
        #maxsa=maxx.splitlines()
        #print('separacion ',maxsa)
        #print('test get ',j.a.get('href'))
        sa=j.get_text( ).splitlines()
        ssa=[x for x in sa if x != '']
        print(" variable ssa  ",type(ssa), "enderecso   ", type(ma))
        print('  ',len(ssa),'    dimns  ',len(ma))
        #print("  ffggh ")
        #print(type(ssa),'   ',len(ssa))
        print(ssa)
        readn(ssa)
        #for lst in ssa:
        #    for j, item in enumerate(lst):
        #        lst[j] = item{1:-5}


        print('line 3  ')
        ol = ol + 1
        if ol == 1:
            break

        frame.append((Statement, Link, Date, Source, Label))
        f.write(Statement.replace(",", "^") + "," + Link + "," + Date.replace(",", "^") + "," + Source.replace(",",
                                                                                                               "^") + "," + Label.replace(
            ",", "^") + "\n")
    upperframe.extend(frame)
f.close()
data = pd.DataFrame(upperframe, columns=['Statement', 'Link', 'Date', 'Source', 'Label'])
data.head()
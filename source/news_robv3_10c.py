import urllib.request, sys, time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import pyttsx3
from nltk.tokenize import sent_tokenize
import os
import json
import datetime
import numpy as np
from urllib.request import Request, urlopen
from spacy.cli.download import download
import nltk

#nltk.download('punkt')
#download(model="en_core_web_sm")



def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def freq(str):
    # break the string into list of words
    str_list = str.split()

    # gives set of unique words
    unique_words = set(str_list)

    for words in unique_words:
        #print()
        print('Frequency of " ', words, '"   is :', str_list.count(words))


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
    #print('processing page :', page)
    url = 'https://www.newsnow.co.uk/h/Business+&+Finance?type=ln'
    print('  webpage  ',url)

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
    #print('tipo   ',type(links))
    #print('how many headlines   ', len(links))
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
       # print('contador  ',ol)
       # print((j))
        #print(' teste salida www.newsnow.co.uk ')
        #print(j.get_text(),'    fghrr ',len(j.get_text()))
        maxx = str(j.findAll("a", {"class": "hll"}))
        #print("  ", type(maxx),'longitud  ',len(maxx))
        #print(" ",type(j.get_text()))
        #print(' long   ',len(maxx),' tipo  ', type(maxx) )
        #print('maxx  ',maxx)
        ind=0
        ma=[]
        while (ind < len(maxx)):
            if 'href' in maxx:
              #match = re.findall(r'\*([^\*]*)\*=', maxx)
              #print('split  ',maxx.index("https"))
              #print('cadena entrada   ',maxx)
              maxx1=maxx[maxx.index("https"):]
              #print(maxx1)
              #print('split  ',maxx.index("https"),'  split2  ', maxx1.index("rel"),'    primera subcadena ',maxx1[0:maxx1.index("rel")-2])
              maxx1=maxx1[maxx1.index("rel")-2:]
              ind=maxx1.index("rel")
              #print('cadena cortada  ',maxx1)
              ma=[ma,maxx1]
              #print("pivot   ",ind)
              maxx=maxx1
            else:
              break
           #input("Press Enter to continue...")
           #print(maxx1[-5:])
           #</a>]


#        print('ma  ', ma)
        #find_all = lambda c, s: [x for x in range(c.find(s), len(c)) if c[x] == s]
        #find_all(sahref,'href=')
        #maxsa=maxx.splitlines()
        #print('separacion ',maxsa)
        #print('test get ',j.a.get('href'))
        sa=j.get_text( ).splitlines()
        ssa=[x for x in sa if x != '']
        #print('cadena completa  ',)\
        ssa = ssa[:len(ssa) - 2]
        cont=1
        for elem in ssa:
            print(cont,')',elem[:-5])
            #print("****")
            a_list = sent_tokenize(elem[:-5])
            #print(' longitud   ', len(a_list))
            #print('  tipo   ', type(a_list))
            #print('cadena ', a_list)
            #freq(j.get_text())
            print('******************')
            print('body ')
            #text_tokens=cleanhtml(str(links))
            #tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
            #print('  tokens   __  ',tokens_without_sw)
            #freq(str(a_list))
            print("************")

            cont=cont+1

    #print(ssa, sep="\n")

        #print("  ffggh ")
        #print('  mamamamamamama ', str(ma))
        cadena=str(ma)
        #print('    ',type((ma)),len((ma)),(ma))
        #print(ma)
        index = 0
        print("inicio busqueda  ")
        #print(str(ma))
        #[i for i in range(len(str(ma))) if str(ma).startswith('https://', i)]
        indexs=[(a.start()) for a in list(re.finditer('https://', str(ma)))]
        indexb=[(b.start()) for b in list(re.finditer('" rel="', str(ma)))]
        indexb=indexb[1:]
        indexs=np.array(indexs)
        indexb=np.array(indexb)

        #print('   ',len(indexs),'   ', len(indexb))
        #print(' aaa  ',(indexs))
        #print(' testando',indexb)
        links=0
        arraylinks=[]
        while links < (len(indexs)):
            #print((indexs[links]))
            print('weblink  ', cadena[indexs[links]:indexb[links]])
            linkext=str(cadena[indexs[links]:indexb[links]])
            arraylinks.append(linkext)
            req = Request(linkext, headers={'User-Agent': 'XYZ/3.0'})
            webpage = urlopen(req, timeout=10).read()
            # fp = urllib.request.urlopen(link.get('href'))
            # print(fp.readlines)
            print(webpage)
            soup = BeautifulSoup(webpage, 'html.parser')
            frame = []
            #linksv = soup.find_all('div', attrs={'330f51f'})
            linksv = soup.find("div", attrs={"divArticleText"})
            #linksv = soup.find('div', {"class": " elementor-widget-container"})
            #print(type(linksv), '   ', len(linksv))
            print((linksv))
            print(cleanhtml(str(linksv)))
            print("****")

            links=links+1


        print('webs extracted  ',links)
        #print('array  ', arraylinks)
        arraylinks = [x for x in arraylinks if x != '']
        #filter(None, arraylinks)
        print('array  ', arraylinks)


        print('cantidad real', len(arraylinks))
        #while index < len(str(ma)):
        #    index = str(ma).find("https://", index)
        #    print(index)
        #    if index == -1:
        #        break
        #print('ll found at', i)
        #index += 2  # +2 because len('ll') == 2

        print("fin busqueda " )
        #print(type(ssa),'   ',len(ssa))
        readn(ssa)

        #for lst in ssa:
        #    for j, item in enumerate(lst):
        #        lst[j] = item{1:-5}


        #print('line 3  ')
        ol = ol + 1
        if ol == 1:
            break

        frame.append((Statement, Link, Date, Source, Label))
        f.write(Statement.replace(",", "^") + "," + Link + "," + Date.replace(",", "^") + "," + Source.replace(",",
                                                                                                               "^") + "," + Label.replace(
            ",", "^") + "\n")
    upperframe.extend(frame)
#f.close()
data = pd.DataFrame(upperframe, columns=['Statement', 'Link', 'Date', 'Source', 'Label'])
data.head()
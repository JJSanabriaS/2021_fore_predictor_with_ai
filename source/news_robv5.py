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
    url = 'https://www.euronews.com/news/business'
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
    links = soup.find_all('div', attrs={'o-block-more-news-themes__articles'})
    #links = soup.find_all('h3', attrs={'m-object__title qa-article-title'})
    #print('tipo   ',(links))
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
        #print(j.get_text())
        print(len(j.get_text()))
        #print(str(j))
        #readn(j)  # leitura audivel computador
        linksv = soup.find_all('h3', attrs={'m-object__title qa-article-title'})
        #print(linksv)
        indexs = [(a.start()) for a in list(re.finditer('href="', str(linksv)))]
        indexb = [(b.start()) for b in list(re.finditer('rel="bookmark"', str(linksv)))]
        #print(indexs,'  dfsfkskfjs ', len(indexs))
        #print(indexb,'  dfsfkskfjsbbbgg ', len(indexb))
        indexs = np.array(indexs)
        indexb = np.array(indexb)
        links = 0
        cadena=str(linksv)
        arraylinks = []
        cadenaextra="https://www.euronews.com"
        while links < (len(indexs)):
            linkext = cadenaextra + cadena[indexs[links] + 6:indexb[links] - 2]
            print('weblink  ',links,')', linkext)
            req = Request(linkext, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req, timeout=10).read()
            #print(webpage)
            soup = BeautifulSoup(webpage, 'html.parser')
            frame = []
            #linksv = soup.find("div", attrs={"c-article-content  js-article-content article__content"})
            linksv = soup.find('div', {"class": "c-article-content"})
            # print(type(linksv), '   ', len(linksv))
            #print((linksv))
            text=cleanhtml(str(linksv))
            #print(' texto   ', text)
            sep=sent_tokenize(text)
            #            print(' texto    ',sep)
            for i in range(len(sep)):
                print(sep[i], end=' ')
                print()

            #print(' tupo ',type(sent_tokenize(text)))
            #print(len(sent_tokenize(text)))
            print("*****************************************************************************************")
            print(' ')
            links=links+1




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
            cont=cont+1




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
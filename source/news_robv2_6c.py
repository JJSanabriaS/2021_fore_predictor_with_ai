#influences Canada	USD/CAD	WTI crude oil and metals
#https://fxssi.com/high-impact-forex-news
#FxSSXI inificator
#Important Meetings: FOMC, ECB, BoE RBA, BoJ
#How often: Monthly

import datetime
import urllib.request, sys, time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import pyttsx3
import os
import json
import datetime
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import urllib.request
from urllib.request import Request, urlopen
import re
import spacy
sp = spacy.load('en_core_web_sm')

all_stopwords = sp.Defaults.stop_words

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
        print('Frequency of ', words, 'is :', str_list.count(words))


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
    url = 'https://www.fxstreet.com'
    print('webpage  ',url)
    x = datetime.datetime.now()
    print(x)

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
    #print('tipo   ',type(links))
    print('how many news headlines  ',len(links))
    print('   ')
    print('   ')
    total=len(links)
    filename = "NEWS.csv"
    f = open(filename, "w", encoding='utf-8')
    headers = "Statement,Link,Date, Source, Label\n"
    f.write(headers)
    Statement=""
    Link=""
    Date=""
    Source=""
    Label=""
    cont=1
    for j in links:
        for link in j.find_all('a'):
            #print('link extraido   ', link.get('href'))
            print(' headline (',cont,'/',total,') --->',j.get_text())
            print(' Link web ---> ',link.get('href'))
            #print(len(j.get_text()))
            readn(j.get_text())
            req = Request(link.get('href'), headers={'User-Agent': 'XYZ/3.0'})
            webpage = urlopen(req, timeout=10).read()
            #fp = urllib.request.urlopen(link.get('href'))
            #print(fp.readlines)
            #print(webpage)
            soup = BeautifulSoup(webpage, 'html.parser')
            frame = []
            links = soup.find_all('div', attrs={'fxs_article_content'})
            #print(type(links),'   ',len(links))
            #print(str(links), ' ',len(str(links)) )
            #print(cleanhtml(str(links)))
            #text = BeautifulSoup(links, "lxml").text
            #print(cleantext)
            #print("****")
            a_list = sent_tokenize(cleanhtml(str(links)))
            #print(' longitud   ', len(a_list))
            #print('  tipo   ', type(a_list))
            #print('cadena ', a_list)
            #freq(j.get_text())
            print('*********************')
            #print('body ')
            text=cleanhtml(str(links))
            #print('text  ',)
            #print(text)
            sep = sent_tokenize(text)
            #print(sep)
            for i in range(len(sep)):
                print(sep[i], end=' ')
                print()

            #freq(text_tokens)
            #for i in range(len(text_tokens)):
            #    print(text_tokens[i], end=' ')
            #    print()

            print("**********************")
            cont=cont+1


    upperframe.extend(frame)
f.close()
data = pd.DataFrame(upperframe, columns=['Statement', 'Link', 'Date', 'Source', 'Label'])
data.head()
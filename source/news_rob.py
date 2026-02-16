import json
import requests
import pyttsx3
import datetime
import os

def readn(nstr):
    engine = pyttsx3.init()

    engine.setProperty('voice', "english")
    engine.setProperty('rate', 150)

    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    engine.say(nstr)
    engine.runAndWait()
    engine.stop()
# https://towardsdatascience.com/scraping-1000s-of-news-articles-using-10-simple-steps-d57636a49755
# https://www.youtube.com/watch?v=5BndsgTuuLg
# https://www.youtube.com/watch?v=1UMHhJEaVTQ
# https://www.tutorialspoint.com/python_text_processing/python_reading_rss_feed.htm
# https://blog.feedspot.com/forex_rss_feeds/
url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=80ce84194eb044458abb49488f793150"
#url="https://www.fxstreet.com/"
r=requests.get(url)
r1=r.text
parsed_news=json.loads(r1)
print(parsed_news)
arts=parsed_news["articles"]
#os.chdir("/home/itachi/Documents/news")
todays_date=str(datetime.date.today())
date_file_name=todays_date+".txt"
fl=open(date_file_name,'w')

for itms in arts:

    fl.write(itms["title"])
    fl.write("\n")
    print(itms["title"])
    readn(itms["title"])
fl.close()

# there can be two options_ read news and create newspaper
# readn(parsed_news)

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import nltk
#nltk.download('punkt')
train=[
    ('According to Gran, the company has no plans to move all production to Russia, although that is where the company is growing','neutral')
    ('For the last quarter of 2010, Componentas net sales doubled to EUR131m from EUR76m for the same period a year earlier , while it moved to a zero pre-tax profit from a pre-tax loss of EUR7m ','positive')
    ('In the third quarter of 2010, net sales increased by 5.2 % to EUR 205.5 mn, and operating profit by 34.9 % to EUR 23.5 mn','positive)
('Operating profit rose to EUR 13.1 mn from EUR 8.7 mn in the corresponding period in 2007 representing 7.7 % of net sales','positive')
('Operating profit totalled EUR 21.1 mn, up from EUR 18.6 mn in 2007, representing 9.7 % of net sales','positive')
('Finnish Talentum reports its operating profit increased to EUR 20.5 mn in 2005 from EUR 9.3 mn in 2004, and net sales totaled EUR 103.3 mn, up from EUR 96.4 mn.','positive')
('Foundries division reports its sales increased by 9.7 % to EUR 63.1 mn from EUR 57.5 mn in the corresponding period in 2006, and sales of the Machine Shop division increased by 16.4 % to EUR 41.2 mn from EUR 35.4 mn in the corresponding period in 2006.','positive')
('Shares closed higher, led by Nokia after it announced plans to team up with Sanyo to manufacture 3G handsets, and by Nokian Tyres after its fourth-quarter earnings report beat analysts expectations , dealers said ','positive')
('Its board of directors will propose a dividend of EUR0 .12 per share for 2010, up from the EUR0 .08 per share paid in 2009',' positive')
('MegaFons subscriber base increased 16.1 % in 2009 to 50.5 million users as of December 31 , while its market share by the number of customers amounted to 24 % as of late 2009 , up from 23 % as of late 2008 , according to TeliaSonera estimates ','positive')
('Net income from life insurance doubled to EUR 6.8 mn from EUR 3.2 mn, and net income from non-life insurance rose to EUR 5.2 mn from EUR 1.5 mn in the corresponding period in 2009.','positive')
('Net sales increased to EUR 193.3 m from EUR 179.9 m and pretax profit rose by 34.2 % to EUR 43.1 m.(EUR1=USD1.4 )','positive')
('Net sales surged by 18.5 % to EUR 167.8 m.Teleste said that EUR 20.4 m, or 12.2 %, of the sales came from the acquisitions made in 2009.','positive')
('Nordea Groups operating profit increased in 2010 by 18 percent year-on-year to 3.64 billion euros and total revenue by 3 percent to 9.33 billion euros ','positive')
('Operating profit for the nine - month period increased from EUR13 .6 m, while net sales increased from EUR394 .7 m, as compared to the corresponding period in 2005',' positive')
('Operating profit for the three - month period increased from EUR1 .2 m, while revenue increased from EUR20 .2 m, as compared to the corresponding period in 2005',' positive')
('The companys net profit rose 11.4 % on the year to 82.2 million euros in 2005 on sales of 686.5 million euros , 13.8 % up on the year , the company said earlier ','positive')
('The Lithuanian beer market made up 14.41 million liters in January, a rise of 0.8 percent from the year-earlier figure, the Lithuanian Brewers Association reporting citing the results from its members','positive')
('Viking Lines cargo revenue increased by 5.4 % to EUR 21.46 mn , and cargo volume increased by 2.4 % to 70,116 cargo units ','positive')
('The fair value of the property portfolio doubled as a result of the Kapiteeli acquisition and totalled EUR2, 686.2 1, 259.7 million.','positive')
('10 February 2011 - Finnish media company Sanoma Oyj HEL: SAA1V said yesterday its 2010 net profit almost tripled to EUR297 .3 m from EUR107.1 m for 2009 and announced a proposal for a raised payout',' positive')
('A Helsinki: ELIiV today reported EPS of EUR1 .13 for 2009, an increase over EPS of EUR1 .12 in 2008',' positive')
('Commission income increased by 22 % to EUR 4.4 mn, and lending volume rose by 13.5 %.','positive')
('In January, traffic, measured in revenue passenger kilometres RPK, went up by 3.2 % and capacity, measured in available seat kilometres ASK, rose by 12.2 %.','positive')
('In January - September 2010, Fiskars  net profit went up by 14 % year-on-year to EUR 65.4 million and net sales to EUR 525.3 million from EUR 487.7 million ','positive')'
('Net income from life insurance rose to EUR 16.5 mn from EUR 14.0 mn, and net income from non-life insurance to EUR 22.6 mn from EUR 15.2 mn in 2009.','positive')
('Sales have risen in other export markets.','positive')
('Sales increased due to growing market rates and increased operations.','positive')
('The agreement strengthens our long - term partnership with Nokia Siemens Networks',' positive')
('The companys order book stood at 1.5 bln euro $ 2.2 bln on September 30 , 2007 , up by 24.2 pct on the year , with international orders amounting to 365 mln euro $ 534.3 mln ','positive')
('The company said that paper demand increased in all of its main markets, including of publication papers, and that it increased average paper prices by 4 percent compared with last year',' positive')
('The worlds second largest stainless steel maker said net profit in the three-month period until Dec. 31 surged to euro603 million US$ 781 million , or euro3 .33 US$ 4.31 per share , from euro172 million , or euro0 .94 per share , the previous year ','positive')
('Shares of Standard Chartered(STAN) rose 1.2 % in the FTSE 100,while Royal Bank of Scotland ( RBS ) shares rose 2 % and Barclays shares ( BARC ) ( BCS ) were up 1.7 %',' positive')
('Shares of Nokia Corp.rose Thursday after the cellphone maker said its third - quarter earnings almost doubled and its share of the global handset market increased.','positive')
('In its financial report, published on Friday, SEB said its net profit soared to SEK6 .745 bn in 2010 from a year earlier SEK 1.114 bn and proposed a 50 % dividend increase to SEK 1.50 per share.','positive')
    ('At the request of Finnish media company Alma Medias newspapers , research manager Jari Kaivo-oja at the Finland Futures Research Centre at the Turku School of Economics has drawn up a future scenario for Finlands national economy by using a model developed by the University of Denver.','neutral')
    ('A maximum of 666, 104 new shares can further be subscribed for by exercising B options under the 2004 stock option plan',' neutral')
    ('Tiimari operates 194 stores in six countries - - including its core Finnish market - - and generated a turnover of 76.5 mln eur in 2005.','neutral')
    ('The acquisition will considerably increase Kemiras sales and market position in the Russian metal industry coatings market ','positive')
    ('In January - September 2007, Finnlines net sales rose to EUR 505.4 mn from EUR 473.5 mn in the corresponding period in 2006 ','positive')
    ('Adjusted for changes in the Group structure, the Divisions net sales increased by 1.7 % ','positive')
('Finnish Aktia Groups operating profit rose to EUR 17.5 mn in the first quarter of 2010 from EUR 8.2 mn in the first quarter of 2009 ','positive')
('Finnish Bank of holands consolidated net operating profit increased from EUR 4.8 mn in the first quarter of 2005 to EUR 6.4 mn in the first quarter of 2006 ','positive')
    ('Finnish financial group Aktia reports operating profit of EUR 44.4 mn in January - September 2009, up from EUR 37.3 mn in the corresponding period in 2008.','positive')
    ('Finnish high technology provider Vaahto Group reports net sales of EUR 41.8 mn in the accounting period September 2007 - February 2008, an increase of 11.2 % from a year earlier.','positive')
    ('Biohit already services many current Genesis customers and the customer base is expected to expand as a result of this agreement.','positive')
    ('Both operating profit and turnover for the three - month period increased, respectively from EUR0 .9 m and EUR8 .3 m, as compared to the corresponding period in 2005',' positive')
    ('Circulation revenue has increased by 5 % in Finland and 4 % in Sweden in 2008.','positive')
    ('Clothing chain Sepps net sales increased by 7.0 % to EUR 30.8 mn ','positive')
    ('Construction volumes meanwhile grow at a rate of 10 - 15 percent annually.','positive')
    ('However, Biohit estimates its total net sales will continue to grow in 2009, and that favourable trends in net sales will lead to a profit in 2009.','positive')
    ('In 2009, Fiskars cash flow from operating activities amounted to EUR121m , up from EUR97m in the previous year ','positive')
    ('In Lithuania, operating profit rose to EUR 190, 000 from EUR 70, 000 in the corresponding period in 2005.','positive')
    ('In the fourth quarter of 2008, net sales increased by 2 % to EUR1, 050.7 mn from EUR1, 027.0 mn in the fourth quarter of 2007.','positive')
    ('International sales rose by 59.8 % to EUR1, 244.4 mn.','positive')
    ('Net sales grew in the period to x20ac 402 million $ 585 US million from x20ac 401 million in 2006.','positive')
    ('Seven-month sales of Ragutis , which is controlled by the Finnish brewery Olvi , declined by 11.2 percent , to 15.41 million liters , and the company held 9.89 percent of the market','negative
('The OMX Helsinki index was down 0.34 pct at 8,256.02 on turnover of 813.191 mln eur','negative')
('Comparable operating profit totaled EUR 4.7 mn , down from EUR 5.1 mn in the corresponding period in 2005 , representing 7.4 % of net sales','negative')
('In Finland 's Hobby Hall 's sales decreased by 10 % , and international sales fell by 19 %','negative')
('In the Baltic states the company reports net sales of EUR 11.9 mn , down from EUR 14.2 mn , and an operative EBIT of EUR -2.2 mn , down from EUR -1.7 mn','negative')
('Operating profits in the half were  0.8 m , down from  0.9 m as Glisten invested in the brand and the management team','negative')
('Sales in Finland decreased by 2.0 % , and international sales decreased by 9.3 % in terms of euros , and by 15.1 % in terms of local currencies','negative')
('Operating result for the 12-month period decreased from the profit of EUR0 .4 m while turnover decreased from EUR5 .6 m , as compared to 2004','negative')
('HELSINKI Thomson Financial - Shares in Cargotec fell sharply in early afternoon trade after the cargo handling group posted a surprise drop in April-June profits , which overshadowed the large number of new orders received during the three months','negative')
('LONDON MarketWatch -- Share prices ended lower in London Monday as a rebound in bank stocks failed to offset broader weakness for the FTSE 100','negative')
('Operating profit fell to EUR 35.4 mn from EUR 68.8 mn in 2007 , including vessel sales gain of EUR 12.3 mn','negative')
('Sales in Finland decreased by 10.5 % in January, while sales outside Finland dropped by 17 %' ,'negative')

]
#train = [
#     ('I love this sandwich.', 'pos'),
#     ('this is an amazing place!', 'pos'),
#     ('I feel very good about these beers.', 'pos'),
#     ('this is my best work.', 'pos'),
#     ("what an awesome view", 'pos'),
#     ('I do not like this restaurant', 'neg'),
#     ('I am tired of this stuff.', 'neg'),
#     ("I can't deal with this", 'neg'),
#     ('he is my sworn enemy!', 'neg'),
#     ('my boss is horrible.', 'neg')
#]

test = [
     ('the beer was good.', 'pos'),
     ('I do not enjoy my job', 'neg'),
     ("I ain't feeling dandy today.", 'neg'),
     ("I feel amazing!", 'pos'),
     ('Gary is a friend of mine.', 'pos'),
     ("I can't believe I'm doing this.", 'neg')
]
#Citi 12.9 pct Citi 16.1 pct
#2. JP Morgan 8.8 pct Deutsche 14.5 pct
#3. UBS 8.8 pct Barclays 8.1 pct
#4. Deutsche 7.9 pct JP Morgan 7.7 pct
#5. BAML 6.4 pct UBS 7.3 pct
#6. Barclays 5.7 pct BAML 6.2 pct
#7. Goldman Sachs 4.7 pct HSBC 5.4 pct
#8. HSBC 4.6 pct BNP Paribas 3.7
#9. XTX Markets 3.9 pct Goldman Sachs 3.4 pct
#10. Morgan Stanley 3.2 pct RBS 3.4 pct

cl = NaiveBayesClassifier(train)
text="FED increase interest rates"
blob = TextBlob(text, classifier=cl)
print(' entrada texto   ',text,'   ')
blob.classify()
print("   segunda evaluacion  ")
prob_dist = cl.prob_classify(text)
print(prob_dist.max())
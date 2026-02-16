from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import nltk
#nltk.download('punkt')
train=[
     ('more vaccinated','pos'),
     (' GDP growth','pos'),
     ('carbon tax law','neg'),
     ('FED is affraid of risk','neg'),
     ('interest rate decreases','pos'),
     ('interest rate increases','neg'),
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
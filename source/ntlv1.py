
#      xbox olx ribeira com quebrado (21) 96730-4585 allan 1000
# xbox flamenco (21) 99709-1581 monica 1000
# xbox madureira (21) 99527-9549 gabi 900
#"<a href=\"https://colab.research.google.com/github/towardsai/tutorials/blob/master/sentiment_analysis_tutorial/sentiment_analysis_tutorial.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
# Sentiment Analysis on Women's Dress Review\r\n",
#       "* Tutorial: https://towardsai.net/p/nlp/sentiment-analysis-opinion-mining-with-python-nlp-tutorial-d1f173ca4e3c\r\n",
#        "* Github: https://github.com/towardsai/tutorials/tree/master/sentyment_analysis_tutorial"
#        "**Download Dataset**"
#        "!wget https://raw.githubusercontent.com/towardsai/tutorials/master/sentiment_analysis_tutorial/women_clothing_review.csv"
#        "**Import All Required Packages**"
import pandas as pd
import numpy as np
import seaborn as sns
import re
import string
from string import punctuation
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.callbacks import EarlyStopping
#"**Read data from csv**"
df = pd.read_csv('women_clothing_review.csv')
df.head()
#        "**Drop unnecessary columns**"
df = df.drop(['Title', 'Positive Feedback Count', 'Unnamed: 0', ], axis=1)
df.dropna(inplace=True)
#        "**Calculation of Polarity**"
df['Polarity_Rating'] = df['Rating'].apply(lambda x: 'Positive' if x > 3 else('Neutral' if x == 3  else 'Negative'))
df.head()
#        "**Plot the Rating visualization graph**"
sns.set_style('whitegrid')
sns.countplot(x='Rating',data=df, palette='YlGnBu_r')
#        "**Plot the Polarity Rating count**"
sns.set_style('whitegrid')
sns.countplot(x='Polarity_Rating',data=df, palette='summer')
#        "**Data Preprocessing**"
df_Positive = df[df['Polarity_Rating'] == 'Positive'][0:8000]
df_Neutral = df[df['Polarity_Rating'] == 'Neutral']
df_Negative = df[df['Polarity_Rating'] == 'Negative']
#        "**Sample negative and neutral polarity dataset and create final dataframe**"
df_Neutral_over = df_Neutral.sample(8000, replace=True)
df_Negative_over = df_Negative.sample(8000, replace=True)
df = pd.concat([df_Positive, df_Neutral_over, df_Negative_over], axis=0)
#        "**Text Preprocessing**"
def get_text_processing(text):
        "    stpword = stopwords.words('english')\n",
        "    no_punctuation = [char for char in text if char not in string.punctuation]\n",
        "    no_punctuation = ''.join(no_punctuation)\n",
        "    return ' '.join([word for word in no_punctuation.split() if word.lower() not in stpword])"
        "**Apply the method \"get_text_processing\" into column review text**"
        df['review'] = df['Review Text'].apply(get_text_processing)
        df.head()
        "**Visualize Text Review with Polarity Rating**"
        df = df[['review', 'Polarity_Rating']]
        df.head()
        "**Apply One hot encoding on negative, neutral, and positive**"
        one_hot = pd.get_dummies(df["Polarity_Rating"])
        df.drop(['Polarity_Rating'],axis=1,inplace=True)
        df = pd.concat([df,one_hot],axis=1)
        df.head()
        "**Apply Train Test Split**"
        X = df['review'].values
        y = df.drop('review', axis=1).values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
        "**Apply vectorization**"
        vect = CountVectorizer()
        X_train = vect.fit_transform(X_train)
        X_test = vect.transform(X_test)
        "**Apply frequency, inverse document frequency:**"
        tfidf = TfidfTransformer()
        X_train = tfidf.fit_transform(X_train)
        X_test = tfidf.transform(X_test)
        X_train = X_train.toarray()
        X_test = X_test.toarray()
        "**Add different layers**"
        model = Sequential()
        #"\n",
        model.add(Dense(units=12673,activation='relu'))
        model.add(Dropout(0.5))
        #"\n",
        model.add(Dense(units=4000,activation='relu'))
        model.add(Dropout(0.5))
        #"\n",
        model.add(Dense(units=500,activation='relu'))
        model.add(Dropout(0.5))
        #"\n",
        model.add(Dense(units=3, activation='softmax'))
        #"\n",
        opt=tf.keras.optimizers.Adam(learning_rate=0.001)
        model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
        #"\n",
        early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=2)
        "**Fit the Model**"
        model.fit(x=X_train, y=y_train, batch_size=256, epochs=100, validation_data=(X_test, y_test), verbose=1, callbacks=early_stop)
        "**Evaluation of Model**"
        model_score = model.evaluate(X_test, y_test, batch_size=64, verbose=1)
        print('Test accuracy:', model_score[1])
        "**Prediction**"
        preds = model.predict(X_test)
        preds

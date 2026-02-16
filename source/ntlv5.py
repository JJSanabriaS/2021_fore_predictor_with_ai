#import spacy
#nlp=spacy.load("en")
#text="santiago es feo"
#sent=nlp(text)

#import en_core_web_sm
#nlp=enc_core_web_sm.load()

import spacy
from spacy.cli.download import download
download(model="en_core_web_sm")

nlp=spacy.load("en_core_web_sm")
text="santiago es feo"
sent=nlp(text)
print(" seccao ", sent[2])
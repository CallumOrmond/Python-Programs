import sklearn 
import spacy 
import math

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import fbeta_score

from sklearn.dummy import DummyClassifier

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

#import nltk
#nltk.download('stopwords')

#TOKENIZER
def text_pipeline_spacy(text):
    tokens = []
    doc = nlp(text)
    for t in doc:
        if not t.is_stop and not t.is_punct and not t.is_space:
            tokens.append(t.lemma_.lower())
    return tokens

nlp = spacy.load('en_core_web_sm', disable=['ner'])
nlp.remove_pipe('tagger')
nlp.remove_pipe('parser')

print(text_pipeline_spacy("He didn't like the U.S. movie 'Snakes on a train, revenge of Viper-man!', now playing in the U.K."))


doc = ["This is the first document"]

one_hot_vectorizer = CountVectorizer(tokenizer=text_pipeline_spacy, binary=True)
print(one_hot_vectorizer.fit(doc).transform(doc))

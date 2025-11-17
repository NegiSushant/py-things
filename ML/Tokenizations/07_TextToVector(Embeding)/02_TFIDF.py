import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
# nltk.download('stopwords')
messages = pd.read_csv("", sep="/t", names=['label', "message"])

# ps=PorterStemmer()
lemmatizer = WordNetLemmatizer()
corpus =[]

for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]','', messages['message'][i])
    review=review.lower()
    review=review.split()

    review = [lemmatizer.lemmatize(word) for word in review if not word in stopwords.words('english')]
    review=' '.join(review)
    corpus.append(review)

print(corpus)

## Create TFIDF And NGrams

tfIdf = TfidfVectorizer(max_features=100)
x = tfIdf.fit_transform(corpus).toarray()

np.set_printoptions(edgeitems=30, linewidth=100000, formatter=dict(float=lambda x:"%.3g" % x))

#N-Grams
tfIdfNg = TfidfVectorizer(max_features=100, ngram_range=(2,2))
y = tfIdf.fit_transform(corpus).toarray()

print(tfIdfNg.vocabulary_)
print(y)
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer


ps = PorterStemmer()
#Loading data from source
messages = pd.read_csv('', sep='\t', names=['label', 'message'])


##Data Cleaning And Preprocessing
corpus =[]
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])
    review = review.lower()
    review=review.split()
    print(review)
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review=' '.join(review)
    corpus.append(review)
print('-----------------------corpus-----------------------')
print(corpus)


## Create the Bag of Words(BOW)
# for binary BOW enable binary=True otherwise leave
cv = CountVectorizer(max_features=2500, binary=True)

x = cv.fit_transform(corpus).toarray()
print('-----------------------transform-----------------------')
print(x)
print(x.shape)

#--------------------N-Gram-------------------
print('-----------------------transform-----------------------')
vocab = cv.vocabulary_
## Create the Bag of Words(BOW) with n-gram
n_cv = CountVectorizer(max_features=200, binary=True, ngram_range=(1,1))
# n_cv = CountVectorizer(max_features=300, binary=True, ngram_range=(1,2))
# n_cv = CountVectorizer(max_features=400, binary=True, ngram_range=(1,3))
# n_cv = CountVectorizer(max_features=400, binary=True, ngram_range=(2,3))
y = n_cv.fit_transform(corpus).toarray()
print(y)
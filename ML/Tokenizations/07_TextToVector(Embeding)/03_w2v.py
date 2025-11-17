import gensim
from gensim.models import Word2Vec, KeyedVectors
import gensim.downloader as api

wv = api.load('word2vec.google-news-300')
vec_king = wv['king']
wv.most_similar('cricket')
wv.similarity("hockey", "sports")
vec = wv['king']-wv['man']+wv['women']

print(vec)

x = wv.most_similar([vec])
print(x)
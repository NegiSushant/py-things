## Lemmatization: technique like stemming, the output we will get after lemmatization is called 'lemma', which is a root word rather then root stem, the output of stemming. After lemmatization, we will be getting a valid word that means the same thing.

## NLTK provides WordNetLemmatizer class which is a thin wrapper arround the wordnet corpus. This class uses morphy() function to the WordNet CorpusReader class to find a lemma.

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
# lemmatizer.lemmatize('word', postword like noun, verb, adjective)
print(lemmatizer.lemmatize('eating', pos='v')) #eat

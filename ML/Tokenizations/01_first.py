from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import wordpunct_tokenize, TreebankWordTokenizer

corpus = "hello My name is Sushant Singh Negi. I'm Full stack AI Engineer. I have knowledge of JavaScript, TypeScript, Java, python, React, Next.JS, Node.js, MongoDB, Express, FastAPI"

# convert the corpus or paragraph into the sentences
documents = sent_tokenize(corpus)
print(type(documents)) #<class 'list'>


for sentence in documents:
    print(sentence)
# hello My name is Sushant Singh Negi.
# I'm Full stack AI Engineer.
# I have knowledge of JavaScript, TypeScript, Java, python, React, Next.JS, Node.js, MongoDB, Express, FastAPI

#--------------------------------------------
##Tokenization
## Paragraph ---> words
## sentence --> words

for sentence in documents:
    print(sentence)
    print(word_tokenize(sentence)) # converting sentence into the word like ['hello', 'My', 'name', 'is', 'Sushant', 'Singh', 'Negi', '.']
    print(wordpunct_tokenize(sentence)) #covert into words and also treat '(apastopi) as word

print('-----------------------------------TreeBankWord------------------')
tokenizer = TreebankWordTokenizer()
print(tokenizer.tokenize(corpus))

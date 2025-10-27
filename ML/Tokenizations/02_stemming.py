# Stemming: process of reducing a word to its word stem that affixes to suffixes and prefixes or to the roots of words khown as a lemma. 
# It is important in natural Language Understanding(NLU) and Natural language Processing(NLP).

# Classification problem
#comments of product is a positive review or negative review
## Reviews ----------> eating, eat, eaten [eat is stemm word]
##

from nltk.stem import PorterStemmer, RegexpStemmer, SnowballStemmer

words = ['eating', 'eats', 'eaten', 'writing', 'writes', 'programming', 'programs', 'history', 'finally', 'finalized']

stemming = PorterStemmer()

for word in words:
    print(word+"----->"+stemming.stem(word))

# eating----->eat
# eats----->eat
# eaten----->eaten
# writing----->write
# writes----->write
# programming----->program
# programs----->program
# history----->histori
# finally----->final
# finalized----->final



# RegexpStemmer class: can easily implement Regular Expression Stemmer algorithms. it takes a single regular expression and removes any prefic or suffix that matches the expression.

reg_stemmer = RegexpStemmer('ing$|s$|e$|e$', min=4)

print(reg_stemmer.stem('eating')) #eat
print(reg_stemmer.stem('ingeating')) #eat
 

##Snowball Stemmer: better than porter stemmer
print('---------------------------------Snowball Stemmer---------------')
snowballSteam = SnowballStemmer('english')

for word in words:
    print(word+"----->"+snowballSteam.stem(word))

# eating----->eat
# eats----->eat
# eaten----->eaten
# writing----->write
# writes----->write
# programming----->program
# programs----->program
# history----->histori
# finally----->final
# finalized----->final
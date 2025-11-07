sentence = 'The Eiffel Tower was built from 1887 to 1889 by French engineer Gustave Eiffel, whose company specialized in building metal frameworks and structures.'

import nltk
# nltk.download('maxent_ne_chunker_tab')
# nltk.download('words')
words = nltk.word_tokenize(sentence)
print(words)

tag_element = nltk.pos_tag(words)
print("tag element: ", tag_element)
nltk.ne_chunk(tag_element).draw()
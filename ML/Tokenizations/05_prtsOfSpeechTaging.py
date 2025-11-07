paragraph = """
My Vision for India — Dr. A.P.J. Abdul Kalam

I have three visions for India. In 3,000 years of our history, people from all over the world have come and invaded us. Yet, we have never invaded anyone. Why? Because we respect the freedom of others. That is why I have my first vision: Freedom. I believe that India must stand up to the world. Unless India stands up, no one will respect us. Freedom is the strength we must protect.

My second vision is Development. For fifty years, we have been a developing nation. It is time we see ourselves as a developed nation. We have the resources, the talent, and the energy to achieve this goal. We must remove corruption, work with integrity, and transform every challenge into an opportunity.

My third vision is Strength. Strength respects strength. We must build our nation in such a way that no one dares to challenge us. Only economic strength and national security can ensure peace and stability.

To realize these visions, every citizen must take responsibility. Don’t say, “What can the government do for me?” Instead, ask, “What can I do for my country?” The dream of a strong, developed, and self-reliant India can come true only if we, the people, believe in it and work for it together.

Remember, the youth of India have the power to change the nation. Dream! Dream transforms into thoughts, and thoughts lead to action. Let’s dream of an India that is fearless, self-reliant, and united — a nation that stands tall in the world.
"""


## Parts Of Speech Tags
import nltk
from nltk.corpus import stopwords
# nltk.download('averaged_perceptron_tagger_eng')
sentences = nltk.sent_tokenize(paragraph)

print(sentences)

#We will find out the Pos Tag
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    print(words)
    words = [word for word in words if word not in set(stopwords.words('english'))]
    pos_tag = nltk.pos_tag(words)
    print(pos_tag)

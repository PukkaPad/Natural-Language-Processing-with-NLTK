from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# stop words: useless words, words  used to fluff up sentences, words used sarcastically, filler words (a, the)

example_sentence = "This is an example showing off stop word filtration."

stop_words = set(stopwords.words("english")) #set of english stop words (already pre-defined)

words = word_tokenize(example_sentence)

filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)
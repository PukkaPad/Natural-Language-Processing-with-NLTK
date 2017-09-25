import nltk
from nltk import sent_tokenize, word_tokenize

# tokenizing:
# word tokenizers: separate by words
# sentence tokenizers: separate by sentence

# lexicon: words and meanings
# corpora: body of text; ex: medical journals, presidential speeches

example_text = "Hello Mr. Smith, how are you doing today? The waeather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard."

#print(sent_tokenize(example_text))
#print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)
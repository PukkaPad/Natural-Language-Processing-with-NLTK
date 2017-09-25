from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# stemming is data preprocessing
# gets the root of words

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

# for w in example_words:
#     print(ps.stem(w))

new_text = "It is very importtant to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)
tokenized = [print (ps.stem(word)) for word in words]

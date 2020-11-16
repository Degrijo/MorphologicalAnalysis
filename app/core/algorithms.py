from re import sub, split
from string import punctuation

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()


def get_key_words(raw_text):
    return {lemmatizer.lemmatize(token.lower()) for token in split(r'[\n ]', sub(f'[{punctuation}]', '', raw_text))
            if token and token not in stopwords.words("english")}

from re import sub, split, search
from string import punctuation

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()


def get_key_words(raw_string):
    return {lemmatizer.lemmatize(token.lower()) for token in split(r'[\n ]', sub(f'[{punctuation}]', '', raw_string))
            if token and token not in stopwords.words("english")}


def extract_keys(text, char):
    found = search(char + r'"[^"]*"', text)
    if found:
        return get_key_words(found.group()[2:-1])
    return set()

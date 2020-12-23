from math import log2
from re import sub, split, search
from string import punctuation

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
from langdetect import detect
from iso639 import languages
from gensim.summarization import summarize, keywords


CHAR_LIMIT = 3
ABSENT_FREQUENCY = 0.1
SUMMARIZE_LIMIT = 10
FR_COMMON_WORDS = {'cette', 'ce', 'cet', 'сes ', 'ma', 'ta', 'sa', 'mon', 'ton', 'son',
                   'mes', 'tes', 'ses', 'notre', 'votre', 'leur', 'nos', 'vos', 'leurs',
                   'un', 'une', 'des', 'du', 'dela', 'le', 'la', 'les', 'au', 'aux',
                   'quel', 'quelle', 'quels', 'quellles', 'de', 'à'}
DE_COMMON_WORDS = {'für', 'durch', 'um', 'ohne', 'gegen', 'die', 'der', 'das', 'aus',
                   'bei', 'nach', 'seit', 'von', 'zu', 'beim', 'vom', 'zum', 'zur',
                   'ein', 'eine', 'und', 'bin', 'bist', 'ist', 'sind', 'ich', 'du', 'auf', 'dass'}
COMMON_WORDS = {'France': FR_COMMON_WORDS, 'Germany': DE_COMMON_WORDS}
lemmatizer = WordNetLemmatizer()


def word_list(raw_string):
    return split(r'[\n ]', sub(f'[{punctuation}]', '', raw_string))


def key_word_list(raw_string):
    tokens = []
    for token in word_list(raw_string):
        if token and token not in stopwords.words("english"):
            tokens.append(lemmatizer.lemmatize(token.lower()))
    return tokens


def extract_key_list(text, char):
    found = search(char + r'"[^"]+"', text)
    if found:
        return key_word_list(found.group()[2:-1])
    return []


def my_case(text):
    return languages.get(alpha2=detect(text)).name


def frequency_word_case(text):
    lemmes = word_list(text)
    fdist = {}
    for lang, words in COMMON_WORDS.items():
        total_prob = 0
        probs = FreqDist(words)
        for lemme in lemmes:
            total_prob += probs[lemme]
        fdist[lang] = total_prob
    return max(fdist.items(), key=lambda x: x[1])[0]


def short_lemme_probabilities(words):
    lemmes = []
    for word in words:
        if len(word) > CHAR_LIMIT:
            for i in range(len(word) - CHAR_LIMIT + 1):
                lemmes.append(word[i:i+CHAR_LIMIT])
        else:
            lemmes.append(word)
    return FreqDist(lemmes)


def short_word_case(text):
    lang_probs = {}
    lemmes = word_list(text)
    for lang, lang_words in COMMON_WORDS.items():
        probs = short_lemme_probabilities(lang_words)
        total_prob = 1
        for lemme in lemmes:
            total_prob *= probs[lemme] or ABSENT_FREQUENCY
        lang_probs[lang] = total_prob
    return max(lang_probs.items(), key=lambda x: x[1])[0]


def get_probs(tokens, doc_count):
    return {word: log2(doc_count / prob) for word, prob in FreqDist(tokens).items()}


def key_words(text):
    return keywords(text, words=SUMMARIZE_LIMIT, split=True)


def custom_summarize(text):
    return ' '.join(summarize(text, split=True))

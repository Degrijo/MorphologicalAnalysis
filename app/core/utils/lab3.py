import nltk
from pymorphy2 import MorphAnalyzer


grammar = r"""
        P: {<PRCL|PREP>}
        V: {<VERB|INFN>}
        N: {<NOUN|NPRO>}
        PP: {<P><N>}
        NP: {<N|PP>+<ADJF|NUMR>+}
        NP: {<ADJF|NUMR>+<N|PP>+}
        VP: {<NP|N><V>}
        VP: {<VP><NP|N|GRND|PRTS|ADVB>}
        VP: {<NP|N|GRND|PRTS|ADVB><VP>}
        VP: {<VP><PP>}
        """
rp = nltk.RegexpParser(grammar)
analyzer = MorphAnalyzer()


def tokenize(sentences):
    return [word for sent in nltk.sent_tokenize(sentences.lower()) for word in nltk.word_tokenize(sent)]


def get_word_tag(text):
    list_word_with_tag = []
    for word in tokenize(text):
        parse_word = analyzer.parse(word)[0]
        list_word_with_tag.append((word, parse_word.tag.POS))
    return list_word_with_tag


def get_tree(text):
    text = text.replace('\n', '')
    if text != '':
        doc = get_word_tag(text)
        new_doc = [item for item in doc if item[0] not in ['.', ',']]
        result = rp.parse(new_doc)
        return result  # pformat

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


def convert_to_tags(text):
    list_word_with_tag = []
    for sentence in nltk.sent_tokenize(text.lower()):
        for word in nltk.word_tokenize(sentence):
            parse_word = analyzer.parse(word)[0]
            if parse_word.tag.POS:
                list_word_with_tag.append((word, parse_word.tag.POS))
    return list_word_with_tag


def get_tree(text):
    text = text.replace('\n', '')
    if text != '':
        new_doc = convert_to_tags(text)
        result = rp.parse(new_doc)
        return result  # pformat
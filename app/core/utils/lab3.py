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


def tokenize(sentences):
    """
    Tokenization of the text.
    :param sentences: entered sentences
    :return: list with words
    """
    list_word = []
    for sent in nltk.sent_tokenize(sentences.lower()):
        for word in nltk.word_tokenize(sent):
            list_word.append(word)
    return list_word


def get_word_tag(text):
    """
    Get word tag using pymorphy2.
    :param text: entered text
    :return: list with words and tags
    """
    list_word_with_tag = []
    list_word = tokenize(text)
    analyzer = MorphAnalyzer()
    for word in list_word:
        parse_word = analyzer.parse(word)[0]
        list_word_with_tag.append((word, parse_word.tag.POS))
    return list_word_with_tag


def draw_tree():
    """
    Function for drawing a tree using a parser for grammar.
    :return: drawing a tree
    """
    text = calculated_text.get(1.0, END)
    text = text.replace('\n', '')
    if text != '':
        doc = get_word_tag(text)
        new_doc = []
        for item in doc:
            if item[0] != ',' and item[0] != '.':
                new_doc.append(item)
        cp = nltk.RegexpParser(grammar)
        result = cp.parse(new_doc)
        result.draw()
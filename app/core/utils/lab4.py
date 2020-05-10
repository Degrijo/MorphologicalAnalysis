from wiki_ru_wordnet import WikiWordnet


def semantic_parse(text):
    wiki_wordnet = WikiWordnet()
    syn = wiki_wordnet.get_synsets(text.lower())
    if syn:
        synonyms = [l.lemma() for l in syn[0].get_words()]
        hyponyms = [hyponym.lemma() for i in wiki_wordnet.get_hyponyms(syn[0]) for hyponym in i.get_words()]
        hypernyms = [hypernym.lemma() for j in wiki_wordnet.get_hypernyms(syn[0]) for hypernym in j.get_words()]
    else:
        synonyms = hyponyms = hypernyms = []
    return {'synonyms': synonyms, 'hyponyms': hyponyms, 'hypernyms': hypernyms}

from re import split
import spacy.tokens.token


POS = {
    "ADJ": "adjective",
    "ADP": "adposition",
    "ADV": "adverb",
    "AUX": "auxiliary",
    "CCONJ": "coordinating conjunction",
    "DET": "determiner",
    "INTJ": "interjection",
    "NOUN": "noun",
    "NUM": "numeral",
    "PART": "particle",
    "PRON": "pronoun",
    "PROPN": "proper noun",
    "PUNCT": "punctuation",
    "SCONJ": "subordinating conjunction",
    "SYM": "symbol",
    "VERB": "verb",
    "X": "other"
}


def process_text(data):
    nlp = spacy.load("en_core_web_sm")
    lemmes = {}
    for sentence in split('[?!.]', data):
        if not sentence:
            continue
        subject = pretext = False
        for token in nlp(sentence):
            if token.is_alpha and token.pos_ in ['PROPN', 'PRON', 'VERB', 'NOUN', 'ADJ', 'ADV', 'AUX']:
                member = None
                if token.pos_ in ['PROPN', 'PRON', 'NOUN']:
                    if pretext or subject:
                        member = 'object'
                    else:
                        member = 'subject'
                        subject = True
                elif token.pos_ in ['VERB', 'AUX']:
                    member = 'predicate'
                elif token.pos_ in ["ADJ"]:
                    member = 'attribute'
                elif token.pos_ in ["ADV"]:
                    member = 'adverbial modifier'
                pretext = False
                if token.lemma_ in lemmes:
                    if member and member not in lemmes[token.lemma_]['proposal_members']:
                        lemmes[token.lemma_]['proposal_members'] += ', ' + member
                else:
                    lemmes[token.lemma_] = {"part_of_speech": POS.get(token.pos_, token.pos_),
                                            "tag": spacy.explain(token.tag_),
                                            "proposal_members": member or '-'}
            if token.pos_ == 'ADP':
                pretext = True
    return sorted(lemmes.items(), key=lambda x: x[0].lower())

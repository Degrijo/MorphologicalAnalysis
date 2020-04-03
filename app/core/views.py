from django.views.generic.edit import FormView
from re import split
import spacy.tokens.token

from app.core.forms import InputForm


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


class LexicalAnalysisView(FormView):
    form_class = InputForm
    template_name = 'input.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_text = process_text(form.cleaned_data['text'])
        return self.render_to_response(self.get_context_data(form=form, new_text=new_text))


def process_text(data):
    nlp = spacy.load("en_core_web_sm")
    lemmes = {}
    for sentence in split('[?!.]', data):
        if not sentence:
            continue
        subject = predicate = union = False
        for token in nlp(sentence):
            if token.is_alpha and token.pos_ in ['PROPN', 'PRON', 'VERB', 'NOUN']:
                member = None
                if token.pos_ in ['PROPN', 'PRON', 'NOUN']:
                    if subject:
                        member = 'object'
                    else:
                        member = 'subject'
                        subject = True
                if token.pos_ == 'VERB':
                    member = 'predicate'
                    predicate = True
                if token.lemma_ in lemmes:
                    if member and member not in lemmes[token.lemma_]['proposal_members']:
                        lemmes[token.lemma_]['proposal_members'] += ', ' + member
                else:
                    lemmes[token.lemma_] = {"part_of_speech": POS.get(token.pos_, token.pos_),
                                            "tag": spacy.explain(token.tag_),
                                            "proposal_members": member or '-'}
    return sorted(lemmes.items(), key=lambda x: x[0].lower())

# subject - подлежащее
# predicate - сказуемое
# object - дополнение
# attribute - определение
# adverbial modifier - обстоятельство

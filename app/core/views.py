from django.views.generic.edit import FormView
from app.core.forms import InputForm

import spacy.tokens.token


DEPS = {
    "ACOMP": "Adjectival complement",
    "ADVCL": "Adverbial clause modifier",
    "ADVMOD": "Adverbial modifier",
    "AGENT": "Agent NN Noun compound modifier",
    "AMOD": "Adjectival modifier",
    "APPOS": "Appositional modifier",
    "ATTR": "Attribute",
    "AUX": "Auxiliary NUM Numeric modifier",
    "AUXPASS": "Auxiliary (passive)",
    "CC": "Coordinating conjunction",
    "CCOMP": "Clausal complement",
    "COMPLM": "Complementizer",
    "CONJ": "Conjunct",
    "CSUBJ": "Clausal subject",
    "CSUBJPASS": "Clausal subject (passive)",
    "DEP": "Unclassified dependent",
    "DET": "Determiner",
    "DOBJ": "Direct object",
    "EXPL": "Expletive",
    "HMOD": "Modifier in hyphenation",
    "HYPH": "Hyphen",
    "INFMOD": "Infinitival modifier",
    "INTJ": "Interjection",
    "IOBJ": "Indirect object",
    "MARK": "Marker",
    "META": "Meta modifier",
    "NEG": "Negation modifier",
    "NMOD": "Modifier of nominal",
    "NPADVMOD": "Noun phrase as ADVMOD",
    "NSUBJ": "Nominal subject",
    "NSUBJPASS": "Nominal subject (passive)",
    "NUMBER": "Number compound modifier",
    "OPRD": "Object predicate",
    "PARATAXIS": "Parataxis",
    "PARTMOD": "Participial modifier",
    "PCOMP": "Complement of a preposition",
    "POBJ": "Object of a preposition",
    "POSS": "Possession modifier",
    "POSSESSIVE": "Possessive modifier",
    "PRECONJ": "Pre-correlative conjunction",
    "PREDET": "Predeterminer",
    "PREP": "Prepositional modifier",
    "PRT": "Particle",
    "PUNCT": "Punctuation",
    "QUANTMOD": "Quantifier phrase modifier",
    "RCMOD": "Relative clause modifier",
    "ROOT": "Root",
    "XCOMP": "Open clausal complement",
}

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

rules = {

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
    lemmes = sorted({token.lemma_ for token in nlp(data) if token.is_alpha}, key=lambda x: x.lower())
    return lemmes

# subject - подлежащее
# predicate - сказуемое
# object - дополнение
# attribute - определение
# adverbial modifier - обстоятельство

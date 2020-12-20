from app.core.models import Document
from app.core.algorithms import extract_keys, get_key_words


MANDATORY_CHAR = r'&'
OPTIONAL_CHAR = r'\|'
UNNECESSARY_CHAR = r'!'


def get_closest_docs(text):
    mandatory = extract_keys(text, MANDATORY_CHAR)
    optional = extract_keys(text, OPTIONAL_CHAR)
    unnecessary = extract_keys(text, UNNECESSARY_CHAR)
    docs = Document.objects.values('text')
    agg_docs = []
    for doc in docs:
        agg_text = get_key_words(doc['text'])
        if not (mandatory - agg_text) and not (unnecessary & agg_text):
            doc['hit_counter'] = len(agg_text & optional) + len(agg_text & mandatory)
            agg_docs.append(doc)
    return sorted(agg_docs, key=lambda obj: obj['hit_counter'], reverse=True)

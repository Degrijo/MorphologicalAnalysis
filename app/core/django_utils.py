from app.core.models import Document
from app.core.algorithms import extract_key_list, key_word_list, get_probs

MANDATORY_CHAR = r'&'
OPTIONAL_CHAR = r'\|'
UNNECESSARY_CHAR = r'!'


def get_closest_docs(text):
    mandatory = extract_key_list(text, MANDATORY_CHAR)
    optional = extract_key_list(text, OPTIONAL_CHAR)
    unnecessary = extract_key_list(text, UNNECESSARY_CHAR)
    docs = Document.objects.values('text')
    count = Document.objects.count()
    agg_docs = []
    query_probs = get_probs(mandatory + optional, count)
    for doc in docs:
        agg_text = key_word_list(doc['text'])
        if not (set(mandatory) - set(agg_text)) and not (set(unnecessary) & set(agg_text)):
            doc_probs = get_probs(agg_text, count)
            total = 0
            for token in mandatory + optional:
                total += query_probs.get(token, 0) * doc_probs.get(token, 0)
            doc['probability'] = total
            agg_docs.append(doc)
    return sorted(agg_docs, key=lambda obj: obj['probability'], reverse=True)

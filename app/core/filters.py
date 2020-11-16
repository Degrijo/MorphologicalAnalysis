from app.core.models import Document
from app.core.algorithms import get_key_words


def get_closest_docs(query):
    key_words = get_key_words(query)
    docs = Document.objects.values('text')
    agg_docs = []
    for doc in docs:
        hit_counter = len(get_key_words(doc['text']) & key_words)
        if hit_counter:
            doc['hit_counter'] = hit_counter
            agg_docs.append(doc)
    return sorted(agg_docs, key=lambda obj: obj['hit_counter'], reverse=True)

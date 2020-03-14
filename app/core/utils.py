from nltk import word_tokenize, pos_tag, tokenize


part_speech_processing = {'CC': {'name': 'coordinating conjunction', 'examples': ['and', 'both', 'but']},
                          'CD': {'name': 'cardinal numeral', 'examples': ['mid-1890', 'nine-thirty', 'forty-two']},
                          'DT': {'name': 'determiner', 'examples': ['all', 'an', 'another']},
                          'EX': {'name': 'existential there', 'examples': ['there']},
                          'FW': {'name': 'foreign word', 'examples': ['gemeinschaft', 'hund', 'ich']},
                          'IN': {'name': 'preposition/subordinating conjunction', 'examples': ['astride', 'among', 'uppon']},
                          'JJ': {'name': 'adjective "big"', 'examples': []},
                          'JJR': {'name': 'adjective, comparative "bigger"', 'examples': []},
                          'JJS': {'name': 'adjective, superlative "biggest"', 'examples': []},
                          'LS': {'name': 'list marker 1)', 'examples': []},
                          'MD': {'name': 'modal could, will', 'examples': []},
                          'NN': {'name': 'common noun', 'examples': ['common-carrier', 'cabbage', 'knuckle-duster']},
                          'NNS': {'name': 'noun plural "desks"', 'examples': []},
                          'NNP': {'name': 'singular proper noun', 'examples': ['Motown', 'Venneboerger', 'Czestochwa']},
                          'NNPS': {'name': 'proper noun, plural "Americans"', 'examples': []},
                          'PDT': {'name': 'predeterminer "all the kids"', 'examples': []},
                          'POS': {'name': "possessive ending parent's", 'examples': []},
                          'PRP': {'name': "personal pronoun", 'examples': ['I', 'he', 'she']},
                          'PRP$': {'name': "possessive pronoun my, his, hers", 'examples': []},
                          'RB': {'name': 'adverb', 'example': ['occasionally', 'unabatingly', 'maddeningly']},
                          'RBR': {'name': 'comparative adverb', 'example': ['better']},
                          'RBS': {'name': 'superlative adverb', 'example': ['better']},
                          'TO': {'name': 'preposition or infinitive marker', 'examples': ['to']},
                          'VB': {'name': 'verb in base form', 'examples': ['ask', 'assemble', 'assess']},
                          }

text = sorted(pos_tag(word_tokenize("""You can strengthen your approach in various ways. You could think more about the grammar
                                of English and add some more rules based on whatever you observe""")),
              key=lambda obj: obj[0].lower())
print(text)

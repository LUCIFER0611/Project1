from nltk.corpus import wordnet

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

# Example Usage
query_terms = ["machine", "learning"]
expanded_terms = []
for term in query_terms:
    expanded_terms.extend(get_synonyms(term))
from pyserini.search import SimpleSearcher

searcher = SimpleSearcher('path_to_index')
hits = searcher.search(query, k=10)

for i in range(len(hits)):
    print(f'{i+1:2} {hits[i].docid:7} {hits[i].score:.5f} {hits[i].raw}')

import spacy
from spacy.symbols import nsubjpass

nlp = spacy.load("en_core_web_sm")

def check(content):
    doc = nlp(content)
    sentences = list(doc.sents)
    passive_count = sum(1 for sent in sentences if any(tok.dep == nsubjpass for tok in sent))
    total_sentences = len(sentences)
    value = (passive_count / total_sentences * 100) if total_sentences else 0
    return {
        "factor": "Passive Voice Usage",
        "value": round(value, 2)
    }

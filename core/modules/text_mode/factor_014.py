import spacy

nlp = spacy.load("en_core_web_sm")

def check(content):
    doc = nlp(content)
    value = sum(1 for tok in doc if tok.pos_ == "ADV")
    return {
        "factor": "Adverb Count",
        "value": value
    }

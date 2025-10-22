import spacy

nlp = spacy.load("en_core_web_sm")
PRONOUNS = {"I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them"}

def check(content):
    doc = nlp(content)
    value = sum(1 for tok in doc if tok.text.lower() in PRONOUNS)
    return {
        "factor": "Pronoun Usage",
        "value": value
    }

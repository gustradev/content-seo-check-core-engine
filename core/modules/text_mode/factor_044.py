# core/modules/text_mode/factor_044.py
import re
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup

SENTENCE_LENGTH_THRESHOLD = 25 # Words

def check(content: str) -> dict:
    """
    Counts sentences that are longer than the defined threshold (25 words).
    """
    value = 0
    if not content:
        return {"factor": "Long Sentences Count", "value": 0}

    clean_text = BeautifulSoup(content, 'html.parser').get_text()
    sentences = sent_tokenize(clean_text)
    
    for sent in sentences:
        words = re.findall(r'\b\w+\b', sent)
        if len(words) > SENTENCE_LENGTH_THRESHOLD:
            value += 1
            
    return {
        "factor": "Long Sentences Count",
        "value": value
    }
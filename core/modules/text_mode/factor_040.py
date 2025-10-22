# core/modules/text_mode/factor_040.py

import re
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup

def check(content: str) -> dict:
    """
    Proxies Clarity by calculating the Average Sentence Length (in words).
    Shorter length correlates with higher clarity.
    """
    value = 0.0
    if not content:
        return {"factor": "Clarity Proxy (Avg Sentence Length)", "value": 0.0}
    
    clean_text = BeautifulSoup(content, 'html.parser').get_text()
    words = re.findall(r'\b\w+\b', clean_text)
    sentences = sent_tokenize(clean_text)

    total_words = len(words)
    total_sentences = len(sentences)

    if total_words > 0 and total_sentences > 0:
        value = total_words / total_sentences
    
    return {
        "factor": "Clarity Proxy (Avg Sentence Length)",
        "value": round(value, 1)
    }
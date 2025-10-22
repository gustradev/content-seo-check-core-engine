# core/modules/text_mode/factor_037.py

# Proxies LSI by counting unique words, assuming higher vocabulary correlates with LSI
import re
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

ENGLISH_STOPWORDS = set(stopwords.words('english'))

def check(content: str) -> dict:
    """
    Proxies LSI by counting the number of unique, non-stop words (unique vocabulary size).
    Higher count suggests broader topical coverage.
    """
    value = 0
    if not content:
        return {"factor": "LSI Proxy (Vocabulary Size)", "value": 0}

    clean_text = BeautifulSoup(content, 'html.parser').get_text()
    words = re.findall(r'\b\w+\b', clean_text.lower())
    
    # Filter out stopwords and count unique remaining words
    unique_words = set(w for w in words if w not in ENGLISH_STOPWORDS)
    value = len(unique_words)
    
    return {
        "factor": "LSI Proxy (Vocabulary Size)",
        "value": value
    }
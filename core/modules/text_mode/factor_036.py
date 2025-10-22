# core/modules/text_mode/factor_036.py

import re
from bs4 import BeautifulSoup

def check(content: str) -> dict:
    """
    Proxies long-tail keywords by counting unique 4-word phrases (quadrigrams).
    Higher count suggests more unique, detailed phrasing.
    """
    value = 0
    if not content:
        return {"factor": "Long-tail Proxy (Unique 4-grams)", "value": 0}

    clean_text = BeautifulSoup(content, 'html.parser').get_text()
    words = re.findall(r'\b\w+\b', clean_text.lower())
    
    quadrigrams = set()
    for i in range(len(words) - 3):
        quadrigrams.add(' '.join(words[i:i+4]))
        
    value = len(quadrigrams)
    
    return {
        "factor": "Long-tail Proxy (Unique 4-grams)",
        "value": value
    }
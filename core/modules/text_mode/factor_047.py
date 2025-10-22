# core/modules/text_mode/factor_047.py

import re
from bs4 import BeautifulSoup

def check(content: str) -> dict:
    """
    Proxies Content Redundancy by calculating the ratio of duplicate 3-word phrases (trigrams).
    Higher ratio means more redundancy.
    """
    value = 0.0
    if not content:
        return {"factor": "Redundancy Proxy (Trigram Ratio)", "value": 0.0}

    clean_text = BeautifulSoup(content, 'html.parser').get_text()
    words = re.findall(r'\b\w+\b', clean_text.lower())
    
    if len(words) < 3:
        return {"factor": "Redundancy Proxy (Trigram Ratio)", "value": 0.0}
        
    all_trigrams = []
    for i in range(len(words) - 2):
        all_trigrams.append(' '.join(words[i:i+3]))
        
    total_trigrams = len(all_trigrams)
    unique_trigrams = len(set(all_trigrams))
    
    # Redundancy is the count of duplicates / total count
    duplicate_count = total_trigrams - unique_trigrams
    value = duplicate_count / total_trigrams
    
    return {
        "factor": "Redundancy Proxy (Trigram Ratio)",
        "value": round(value, 2)
    }
# core/modules/text_mode/factor_042.py

import re

def check(content: str) -> dict:
    """
    Proxies Grammar Errors by calculating the Average Word Length.
    Longer words might indicate technical/complex language (less 'smooth').
    """
    value = 0.0
    if not content:
        return {"factor": "Grammar Proxy (Avg Word Length)", "value": 0.0}

    words = re.findall(r'\b\w+\b', content)
    total_words = len(words)
    total_length = sum(len(word) for word in words)
    
    if total_words > 0:
        value = total_length / total_words

    return {
        "factor": "Grammar Proxy (Avg Word Length)",
        "value": round(value, 2)
    }
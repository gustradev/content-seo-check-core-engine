# core/modules/text_mode/factor_038.py

import re

PLACEHOLDER_KEYWORD = "seo" 

def check(content: str) -> dict:
    """
    Proxies Semantic Relevance by calculating Primary Keyword Density (percentage of total words).
    """
    value = 0.0
    if not content or not PLACEHOLDER_KEYWORD:
        return {"factor": "Semantic Relevance Proxy (Keyword Density)", "value": 0.0}

    words = re.findall(r'\b\w+\b', content.lower())
    total_words = len(words)
    
    if total_words > 0:
        keyword_lower = PLACEHOLDER_KEYWORD.lower()
        keyword_count = sum(1 for word in words if word == keyword_lower)
        value = (keyword_count / total_words) * 100
    
    return {
        "factor": "Semantic Relevance Proxy (Keyword Density)",
        "value": round(value, 2)
    }
# core/modules/text_mode/factor_034.py
import re

PLACEHOLDER_KEYWORD = "seo" 

def check(content: str) -> dict:
    """
    Calculates the percentage of keyword occurrences that are in the first 10% of the text.
    """
    value = 0.0
    if not content or not PLACEHOLDER_KEYWORD:
        return {"factor": "Keyword Prominence (Start)", "value": 0.0}

    words = re.findall(r'\b\w+\b', content.lower())
    keyword_lower = PLACEHOLDER_KEYWORD.lower()
    
    total_words = len(words)
    if total_words == 0:
        return {"factor": "Keyword Prominence (Start)", "value": 0.0}

    first_10_percent_index = int(total_words * 0.10)
    
    total_keyword_count = sum(1 for word in words if word == keyword_lower)
    
    if total_keyword_count == 0:
        return {"factor": "Keyword Prominence (Start)", "value": 0.0}

    prominent_keyword_count = sum(1 for word in words[:first_10_percent_index] if word == keyword_lower)

    # Percentage of *all* keyword occurrences found in the first 10%
    value = (prominent_keyword_count / total_keyword_count) * 100
    
    return {
        "factor": "Keyword Prominence (Start)",
        "value": round(value, 1)
    }
# core/modules/text_mode/factor_035.py
import re
import numpy as np
from bs4 import BeautifulSoup

PLACEHOLDER_KEYWORD = "content"

def check(content: str) -> dict:
    """
    Measures the Coefficient of Variation of keyword appearances across paragraphs.
    Lower ratio (closer to 0) means better, more even distribution.
    """
    value = 0.0
    if not content or not PLACEHOLDER_KEYWORD:
        return {"factor": "Keyword Distribution (CoV)", "value": 0.0}

    clean_text = BeautifulSoup(content, 'html.parser').get_text()
    paragraphs = [p.strip() for p in clean_text.split('\n\n') if p.strip()]
    
    if len(paragraphs) < 2:
        return {"factor": "Keyword Distribution (CoV)", "value": 0.0}

    keyword_lower = PLACEHOLDER_KEYWORD.lower()
    counts = []

    for p in paragraphs:
        words = re.findall(r'\b\w+\b', p.lower())
        count = sum(1 for word in words if word == keyword_lower)
        counts.append(count)

    # Calculate Coefficient of Variation (Std Dev / Mean)
    if counts and np.mean(counts) > 0:
        std_dev = np.std(counts)
        mean_count = np.mean(counts)
        value = std_dev / mean_count
    
    return {
        "factor": "Keyword Distribution (CoV)",
        "value": round(value, 2)
    }
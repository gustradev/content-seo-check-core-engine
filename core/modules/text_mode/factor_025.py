# core/modules/text_mode/factor_025.py
import re

# WARNING: In a real system, the KEYWORD should be passed to check() or fetched dynamically.
PLACEHOLDER_KEYWORD = "content"

def check(content: str) -> dict:
    """
    Checks if the Primary Keyword appears within the last 100 words of the text.
    Returns 1 if found, 0 otherwise.
    """
    value = 0
    if content and PLACEHOLDER_KEYWORD:
        # Simple word tokenization
        words = re.findall(r'\b\w+\b', content.lower())
        
        # Take the last 100 words
        last_100_words = words[-100:]
        keyword_lower = PLACEHOLDER_KEYWORD.lower()
        
        if keyword_lower in last_100_words:
            value = 1

    return {
        "factor": "Keyword in Last 100 Words",
        "value": value
    }
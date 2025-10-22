# core/modules/text_mode/factor_041.py

import re
# Placeholder for a very basic dictionary check (NOT A ROBUST SPELL CHECKER)
# For a real project, use 'pyspellchecker' and instruct user to install it.
BASIC_DICTIONARY = {"the", "a", "is", "content", "check", "seo", "engine", "text", "mode", "url"} 

def check(content: str) -> dict:
    """
    Counts spelling errors by checking words against a very basic internal dictionary.
    (Highly unreliable, use 'pyspellchecker' for production).
    """
    value = 0
    if not content:
        return {"factor": "Spelling Errors Count (Basic Proxy)", "value": 0}
    
    words = re.findall(r'\b\w+\b', content.lower())
    
    # Misspelled are words NOT in the basic dictionary
    misspelled_count = sum(1 for word in words if word not in BASIC_DICTIONARY)
    value = misspelled_count

    return {
        "factor": "Spelling Errors Count (Basic Proxy)",
        "value": value
    }
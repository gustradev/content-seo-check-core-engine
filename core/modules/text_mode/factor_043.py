# core/modules/text_mode/factor_043.py

from nltk.tokenize import sent_tokenize
import re
from bs4 import BeautifulSoup

def check(content: str) -> dict:
    """
    Checks Punctuation Accuracy by finding the ratio of sentences ending with terminal punctuation.
    (Should be close to 1.0).
    """
    value = 0.0
    if not content:
        return {"factor": "Punctuation Accuracy (Terminal)", "value": 0.0}

    clean_text = BeautifulSoup(content, 'html.parser').get_text()
    sentences = sent_tokenize(clean_text)
    total_sentences = len(sentences)

    if total_sentences > 0:
        correct_ending_count = 0
        terminal_regex = re.compile(r'(\.|\?|!)\s*$') # Ends with period, question mark, or exclamation
        
        for sent in sentences:
            if terminal_regex.search(sent.strip()):
                correct_ending_count += 1
                
        value = correct_ending_count / total_sentences
    
    return {
        "factor": "Punctuation Accuracy (Terminal)",
        "value": round(value, 2)
    }
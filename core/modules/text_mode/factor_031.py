# core/modules/text_mode/factor_031.py
import re
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup

# --- Helper function for syllable counting (simple heuristic) ---
def count_syllables(word):
    word = word.lower()
    if len(word) <= 3:
        return 1
    # Simple rule: count vowels (a, e, i, o, u, y) but remove trailing 'e' and double vowels
    word = re.sub(r'e$', '', word)
    word = re.sub(r'[aeiouy]+', 'a', word)
    return max(1, len(word))

def check(content: str) -> dict:
    """
    Calculates the Flesch-Kincaid Grade Level.
    """
    value = 0.0
    if not content:
        return {"factor": "Readability Level (Grade)", "value": 0.0}

    # Strip HTML tags
    clean_text = BeautifulSoup(content, 'html.parser').get_text()

    words = re.findall(r'\b\w+\b', clean_text)
    
    # NLTK sentence tokenization is reliable
    sentences = sent_tokenize(clean_text)

    total_words = len(words)
    total_sentences = len(sentences)
    total_syllables = sum(count_syllables(word) for word in words)

    if total_words > 0 and total_sentences > 0:
        # Flesch-Kincaid Grade Level Formula
        avg_sentence_length = total_words / total_sentences
        avg_syllables_per_word = total_syllables / total_words
        
        value = 0.39 * avg_sentence_length + 11.8 * avg_syllables_per_word - 15.59
    
    return {
        "factor": "Readability Level (Grade)",
        "value": round(value, 1)
    }
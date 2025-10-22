# core/modules/text_mode/factor_032.py

from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup

def check(content: str) -> dict:
    """
    Measures internal originality by checking the ratio of unique sentences.
    Higher value (closer to 1.0) means higher originality/lower internal redundancy.
    """
    value = 0.0
    if not content:
        return {"factor": "Content Originality (Internal)", "value": 0.0}
    
    clean_text = BeautifulSoup(content, 'html.parser').get_text()
    sentences = [s.strip().lower() for s in sent_tokenize(clean_text) if s.strip()]
    
    total_sentences = len(sentences)
    if total_sentences > 0:
        unique_sentences = len(set(sentences))
        value = unique_sentences / total_sentences

    return {
        "factor": "Content Originality (Internal)",
        "value": round(value, 2)
    }
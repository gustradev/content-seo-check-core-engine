# core/modules/text_mode/factor_050.py
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup

MAX_INTERNAL_COMMAS = 1 

def check(content: str) -> dict:
    """
    Proxies Sentence Simplicity by calculating the percentage of sentences 
    with one or zero internal commas (a rough indicator of simple structure).
    """
    value = 0.0
    if not content:
        return {"factor": "Simple Sentence Percentage Proxy", "value": 0.0}

    clean_text = BeautifulSoup(content, 'html.parser').get_text()
    sentences = sent_tokenize(clean_text)
    total_sentences = len(sentences)
    simple_sentence_count = 0
    
    if total_sentences > 0:
        for sent in sentences:
            comma_count = sent.count(',')
            
            if comma_count <= MAX_INTERNAL_COMMAS:
                simple_sentence_count += 1
                
        value = (simple_sentence_count / total_sentences) * 100
    
    return {
        "factor": "Simple Sentence Percentage Proxy",
        "value": round(value, 1)
    }
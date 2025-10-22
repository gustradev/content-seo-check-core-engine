# core/modules/text_mode/factor_029.py
import re
from nltk.tokenize import sent_tokenize

# NOTE: This requires 'punkt' data from NLTK. User must run: 
# import nltk; nltk.download('punkt') 
# at least once.

def check(content: str) -> dict:
    """
    Measures sentence length variety using the ratio of unique sentence lengths 
    to the total number of sentences. A higher value (closer to 1.0) indicates 
    higher variety.
    """
    value = 0.0
    if not content:
        return {"factor": "Sentence Variety", "value": 0.0}

    # 1. Strip HTML tags from content to get pure text for sentence tokenization
    try:
        from bs4 import BeautifulSoup
        clean_text = BeautifulSoup(content, 'html.parser').get_text()
    except ImportError:
        # Fallback if BeautifulSoup isn't available
        clean_text = content 

    # 2. Tokenize into sentences
    sentences = sent_tokenize(clean_text)
    total_sentences = len(sentences)

    if total_sentences > 1:
        sentence_lengths = []
        for sent in sentences:
            # Count words in the sentence
            word_count = len(re.findall(r'\b\w+\b', sent))
            sentence_lengths.append(word_count)
            
        unique_lengths = len(set(sentence_lengths))
        
        # Variety is Unique Lengths / Total Sentences
        value = unique_lengths / total_sentences
        
    return {
        "factor": "Sentence Variety",
        "value": round(value, 2)
    }
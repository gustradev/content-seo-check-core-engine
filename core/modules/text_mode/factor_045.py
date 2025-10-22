# core/modules/text_mode/factor_045.py
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# --- NOTE: Requires nltk.download('stopwords') and nltk.download('punkt') ---
ENGLISH_STOPWORDS = set(stopwords.words('english'))

def check(content: str) -> dict:
    """
    Calculates the ratio of stopwords to total words.
    """
    value = 0.0
    if not content:
        return {"factor": "Stopword Ratio", "value": 0.0}

    words = word_tokenize(content.lower())
    filtered_words = [w for w in words if re.match(r'\w+', w)]
    
    total_words = len(filtered_words)
    if total_words == 0:
        return {"factor": "Stopword Ratio", "value": 0.0}

    stopword_count = sum(1 for word in filtered_words if word in ENGLISH_STOPWORDS)
    
    value = stopword_count / total_words
    
    return {
        "factor": "Stopword Ratio",
        "value": round(value, 2)
    }
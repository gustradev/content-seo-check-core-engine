# core/modules/text_mode/factor_030.py
import re

def check(content: str) -> dict:
    """
    Calculates the average word count per paragraph.
    (Assumes paragraphs are separated by two or more newlines or typical HTML tags like <p>).
    """
    value = 0
    if not content:
        return {"factor": "Average Paragraph Length", "value": 0}

    # 1. Strip HTML tags to get pure text
    try:
        from bs4 import BeautifulSoup
        clean_text = BeautifulSoup(content, 'html.parser').get_text()
    except ImportError:
        clean_text = content
        
    # 2. Split by one or more blank lines (robust paragraph separation)
    paragraphs = [p.strip() for p in clean_text.split('\n\n') if p.strip()]
    total_paragraphs = len(paragraphs)
    
    if total_paragraphs > 0:
        total_word_count = 0
        
        for p in paragraphs:
            # Count words in the paragraph
            words = re.findall(r'\b\w+\b', p)
            total_word_count += len(words)
            
        # Calculate average word count per paragraph
        value = total_word_count / total_paragraphs
        
    return {
        "factor": "Average Paragraph Length",
        "value": round(value)
    }
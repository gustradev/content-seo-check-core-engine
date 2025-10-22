# core/modules/text_mode/factor_049.py
from bs4 import BeautifulSoup
import re

def check(content: str) -> dict:
    """
    Calculates the average word count of all H2 and H3 subheadings.
    """
    value = 0.0
    if not content:
        return {"factor": "Average Subheading Length", "value": 0.0}

    try:
        soup = BeautifulSoup(content, 'html.parser')
        subheadings = soup.find_all(['h2', 'h3'])
        
        total_subheadings = len(subheadings)
        total_words = 0
        
        if total_subheadings > 0:
            for tag in subheadings:
                if tag.text:
                    words = re.findall(r'\b\w+\b', tag.text)
                    total_words += len(words)
                    
            value = total_words / total_subheadings
            
    except Exception:
        pass
        
    return {
        "factor": "Average Subheading Length",
        "value": round(value, 1)
    }
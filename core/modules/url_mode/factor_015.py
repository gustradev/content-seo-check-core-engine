# core/modules/url_mode/factor_015.py
from bs4 import BeautifulSoup
import re

def check(html: str) -> dict:
    """
    Counts the total visible words on the page, excluding scripts and styles.
    """
    value = 0
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            
            # Remove script and style elements
            for script_or_style in soup(['script', 'style', 'head']):
                script_or_style.decompose()
            
            text = soup.get_text()
            
            # Tokenize by word
            words = re.findall(r'\b\w+\b', text)
            value = len(words)
        except Exception:
            pass

    return {
        "factor": "Word Count",
        "value": value
    }
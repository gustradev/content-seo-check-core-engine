# core/modules/url_mode/factor_016.py
from bs4 import BeautifulSoup
import re

def check(html: str) -> dict:
    """
    Calculates the ratio of visible text size (bytes) to total HTML size (bytes).
    Returns a percentage (0-100).
    """
    value = 0.0
    if html:
        try:
            # Use raw byte size of the HTML input
            total_html_size = len(html.encode('utf-8'))
            
            if total_html_size > 0:
                soup = BeautifulSoup(html, 'html.parser')
                
                # Remove non-visible/code elements
                for script_or_style in soup(['script', 'style', 'head', 'noscript']):
                    script_or_style.decompose()
                
                text = soup.get_text()
                
                # Clean up text (normalize whitespace)
                clean_text = re.sub(r'\s+', ' ', text).strip()
                visible_text_size = len(clean_text.encode('utf-8'))
                
                value = (visible_text_size / total_html_size) * 100
        except Exception:
            pass

    return {
        "factor": "Text-to-HTML Ratio",
        "value": round(value, 1)
    }
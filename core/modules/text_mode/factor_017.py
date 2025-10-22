# core/modules/text_mode/factor_017.py
from bs4 import BeautifulSoup

def check(content: str) -> dict:
    """
    Counts the total number of H2 and H3 subheadings in the content (requires HTML parsing).
    """
    value = 0
    if content:
        try:
            soup = BeautifulSoup(content, 'html.parser')
            h2_count = len(soup.find_all('h2'))
            h3_count = len(soup.find_all('h3'))
            value = h2_count + h3_count
        except Exception:
            # Silently handle parsing errors, return 0, let analyzer log the error if needed
            pass

    return {
        "factor": "Subheading Count (H2/H3)",
        "value": value
    }
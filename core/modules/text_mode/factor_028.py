# core/modules/text_mode/factor_028.py
from bs4 import BeautifulSoup

def check(content: str) -> dict:
    """
    Calculates the ratio of unique anchor texts to total links (0.0 to 1.0).
    A value closer to 1.0 means high diversity.
    """
    value = 0.0
    if content:
        try:
            soup = BeautifulSoup(content, 'html.parser')
            links = soup.find_all('a')
            total_links = len(links)
            
            if total_links > 0:
                anchor_texts = set()
                for link in links:
                    # Clean the anchor text (lower case, strip whitespace)
                    text = link.get_text().strip().lower()
                    if text: # Ignore links with no visible anchor text
                        anchor_texts.add(text)
                        
                unique_texts = len(anchor_texts)
                value = unique_texts / total_links
                
        except Exception:
            pass

    return {
        "factor": "Anchor Text Diversity",
        "value": round(value, 2)
    }
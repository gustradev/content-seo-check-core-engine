# core/modules/url_mode/factor_030.py
from bs4 import BeautifulSoup

# Generic anchor text phrases (case-insensitive and must match exactly)
# A high ratio of these indicates poor SEO optimization.
GENERIC_ANCHORS = {
    "click here", "read more", "learn more", "here", 
    "this link", "more", "download", "view details", 
    "go", "link", "details"
}

def check(html: str) -> dict:
    """
    Calculates the ratio of generic anchor texts (e.g., "click here") to the total 
    number of unique links found on the page.
    Returns a percentage (0-100). Higher value indicates poorer optimization.
    """
    value = 0.0
    if not html:
        return {"factor": "Generic Anchor Text Ratio", "value": 0.0}

    try:
        soup = BeautifulSoup(html, 'html.parser')
        # Find all anchor tags that have an 'href' attribute
        links = soup.find_all('a', href=True)
        total_links = len(links)
        
        if total_links == 0:
            return {"factor": "Generic Anchor Text Ratio", "value": 0.0}
            
        generic_count = 0
        for link in links:
            # Get the anchor text, strip whitespace, and normalize to lowercase
            anchor_text = link.get_text().strip().lower()
            
            # Check if the cleaned text matches any generic phrases
            if anchor_text in GENERIC_ANCHORS:
                generic_count += 1
                
        # Calculate the ratio as a percentage
        value = (generic_count / total_links) * 100
        
    except Exception:
        # Fail gracefully if parsing encounters an error
        pass

    return {
        "factor": "Generic Anchor Text Ratio",
        "value": round(value, 1)
    }
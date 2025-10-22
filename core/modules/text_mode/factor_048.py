# core/modules/text_mode/factor_048.py
from bs4 import BeautifulSoup

def check(content: str) -> dict:
    """
    Counts major breaks in heading hierarchy (e.g., H1 followed immediately by H3).
    """
    value = 0
    if not content:
        return {"factor": "Heading Hierarchy Violations", "value": 0}

    try:
        soup = BeautifulSoup(content, 'html.parser')
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        
        def get_level(tag):
            return int(tag.name[1])

        last_level = 0 # Start before H1
        for heading in headings:
            current_level = get_level(heading)
            
            # Violation 1: Start must be H1
            if last_level == 0 and current_level > 1:
                value += 1
            
            # Violation 2: Skipping a level (H2 -> H4)
            if last_level > 0 and current_level > last_level + 1:
                value += 1 

            last_level = current_level
            
    except Exception:
        pass
        
    return {
        "factor": "Heading Hierarchy Violations",
        "value": value
    }
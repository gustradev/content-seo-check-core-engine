# core/modules/url_mode/factor_017.py
from bs4 import BeautifulSoup
import re

# Placeholder URL structure for internal simulation
PLACEHOLDER_URL_PATH = "/example-article-title-from-meta-description-here/"

def check(html: str) -> dict:
    """
    Proxies the "Keyword in URL" check by extracting the Meta Description content 
    and checking if its normalized text is present in a placeholder URL path.
    Returns 1 if a match is found, 0 otherwise.
    """
    value = 0
    if not html:
        return {"factor": "Keyword in URL (Meta Description Proxy)", "value": 0}

    try:
        soup = BeautifulSoup(html, 'html.parser')
        
        # 1. Extract the Meta Description content
        meta_desc_tag = soup.find('meta', attrs={'name': 'description'})
        meta_desc = meta_desc_tag.get('content', '').strip().lower() if meta_desc_tag else None
        
        if meta_desc:
            # 2. Normalize the description content for a pseudo-URL check
            # We take the first 5 words, remove stopwords, and slugify
            from nltk.corpus import stopwords
            from nltk.tokenize import word_tokenize
            
            # Ensure NLTK data is downloaded (requires pre-run setup)
            try:
                stop_words = set(stopwords.words('english'))
            except LookupError:
                # Fallback if stopwords not downloaded
                stop_words = set() 

            words = word_tokenize(meta_desc)
            
            # Create a slug from the first few non-stop words
            slug_words = [w for w in words if w.isalnum() and w not in stop_words][:5]
            
            if slug_words:
                slug_fragment = '-'.join(slug_words)
                
                # 3. Check if this fragment is in the placeholder URL path
                # This simulates having a slugified keyword in the URL
                if slug_fragment in PLACEHOLDER_URL_PATH:
                    value = 1
            
    except Exception:
        pass

    return {
        "factor": "Keyword in URL (Meta Description Proxy)",
        "value": value
    }
# core/modules/url_mode/factor_020.py

def check(html: str) -> dict:
    """
    Robots.txt check requires accessing the site's root path over the network 
    to verify presence and content. Cannot be measured internally from HTML content.
    Returns 0, indicating the value is unavailable without Premium Plus Access.
    """
    value = 0 

    return {
        "factor": "Robots.txt Check (Requires Premium Plus Access)",
        "value": value
    }
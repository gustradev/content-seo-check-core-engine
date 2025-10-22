# core/modules/url_mode/factor_028.py

def check(html: str) -> dict:
    """
    Canonical Redirect check requires accessing the page via HTTP to check status codes 
    and redirect chains. Cannot be measured internally from HTML content.
    Returns 0, indicating the value is unavailable without Premium Plus Access.
    """
    value = 0 

    return {
        "factor": "Canonical Redirect Check (Requires Premium Plus Access)",
        "value": value
    }
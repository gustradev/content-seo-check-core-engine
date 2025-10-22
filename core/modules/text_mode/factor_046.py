# core/modules/text_mode/factor_046.py

import re
from bs4 import BeautifulSoup

def check(content: str) -> dict:
    """
    Proxies Content Gap by calculating the Average Paragraph Length (in words) from Factor 030.
    """
    from core.modules.text_mode import factor_030 
    
    value = factor_030.check(content).get("value", 0.0)
    
    return {
        "factor": "Content Gap Proxy (Avg Paragraph Length)",
        "value": round(value, 1)
    }
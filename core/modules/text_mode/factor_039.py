# core/modules/text_mode/factor_039.py

from core.modules.text_mode.factor_016 import TRANSITION_WORDS # Reuse F016 logic
import re

def check(content: str) -> dict:
    """
    Proxies Coherence by calculating the Transition Word Ratio (from Factor 016 logic).
    Higher ratio suggests better flow.
    """
    value = 0.0
    if not content:
        return {"factor": "Coherence Proxy (Transition Ratio)", "value": 0.0}

    words = re.findall(r'\b\w+\b', content.lower())
    word_count = len(words)
    
    if word_count > 0:
        transition_count = sum(1 for word in words if word in TRANSITION_WORDS)
        value = transition_count / word_count
    
    return {
        "factor": "Coherence Proxy (Transition Ratio)",
        "value": round(value, 2)
    }
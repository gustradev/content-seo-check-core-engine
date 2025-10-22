# core/modules/text_mode/factor_016.py
import re

TRANSITION_WORDS = {
    "also", "and", "but", "however", "therefore", "thus", "consequently", 
    "moreover", "furthermore", "in addition", "similarly", "likewise", 
    "meanwhile", "next", "finally", "in conclusion", "for example", 
    "for instance", "specifically", "in contrast", "conversely"
}

def check(content: str) -> dict:
    """
    Calculates the percentage of transition words in the content.
    """
    if not content:
        return {"factor": "Transition Words Usage", "value": 0.0}

    # Simple word tokenization
    words = re.findall(r'\b\w+\b', content.lower())
    
    word_count = len(words)
    if word_count == 0:
        return {"factor": "Transition Words Usage", "value": 0.0}

    transition_count = sum(1 for word in words if word in TRANSITION_WORDS)
    
    # Calculate percentage (Transition Count / Word Count * 100)
    percentage = (transition_count / word_count) * 100
    
    return {
        "factor": "Transition Words Usage",
        "value": round(percentage, 2)
    }
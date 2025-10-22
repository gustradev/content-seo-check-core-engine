import re

STOPWORDS = {"the", "is", "in", "and", "of", "to", "a", "that", "it", "on", "for", "as", "with", "this", "by"}

def check(content: str):
    words = re.findall(r'\b\w+\b', content.lower())
    total = len(words)
    stop_count = sum(1 for w in words if w in STOPWORDS)
    ratio = stop_count / total if total > 0 else 0
    return {
        "factor": "Stopword Ratio",
        "value": round(ratio, 2)
    }

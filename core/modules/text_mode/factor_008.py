import re

SECONDARY_KEYWORDS = ["seo", "optimization", "content"]  # 🔧 example keywords

def check(content: str):
    words = re.findall(r'\b\w+\b', content.lower())
    total = len(words)
    count = sum(words.count(k) for k in SECONDARY_KEYWORDS)
    density = (count / total) * 100 if total > 0 else 0
    return {
        "factor": "Keyword Density (Secondary)",
        "value": round(density, 2)
    }

import re

PRIMARY_KEYWORD = "ai"  # 🔧 can be dynamically set later

def check(content: str):
    words = re.findall(r'\b\w+\b', content.lower())
    total = len(words)
    count = words.count(PRIMARY_KEYWORD.lower())
    density = (count / total) * 100 if total > 0 else 0
    return {
        "factor": "Keyword Density (Primary)",
        "value": round(density, 2)
    }

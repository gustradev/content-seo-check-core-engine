def check(content):
    words = content.lower().split()
    unique_words = set(words)
    return {
        "factor": "Unique Words Count",
        "score": len(unique_words)
    }

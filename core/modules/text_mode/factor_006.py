def check(content: str):
    words = [w for w in content.split() if w.isalpha()]
    avg_word_len = sum(len(w) for w in words) / len(words) if words else 0
    return {
        "factor": "Average Word Length",
        "value": round(avg_word_len, 2)
    }

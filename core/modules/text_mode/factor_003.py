def check(content):
    words = content.split()
    avg_len = sum(len(w) for w in words) / max(len(words), 1)
    return {
        "factor": "Average Word Length",
        "score": round(avg_len, 2)
    }

STOPWORDS = {"the","and","is","in","it","of","to","a","for","on"}

def check(content):
    words = content.lower().split()
    stop_count = sum(1 for w in words if w in STOPWORDS)
    ratio = stop_count / max(len(words), 1) * 100
    return {
        "factor": "Stopword Ratio",
        "score": round(ratio, 2)
    }

def check(content):
    words = content.split()
    return {
        "factor": "Word Count",
        "score": len(words)
    }

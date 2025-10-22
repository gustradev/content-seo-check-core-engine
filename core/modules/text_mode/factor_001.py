def check(content: str):
    words = content.split()
    return {
        "factor": "Word Count",
        "value": len(words)
    }

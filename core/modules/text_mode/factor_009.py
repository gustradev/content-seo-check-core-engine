def check(content):
    count = content.count('?')
    return {
        "factor": "Number of Questions",
        "score": count
    }

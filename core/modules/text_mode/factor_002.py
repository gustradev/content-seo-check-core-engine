import re
def check(content):
    sentences = re.split(r'[.!?]+', content)
    sentences = [s.strip() for s in sentences if s.strip()]
    return {
        "factor": "Sentence Count",
        "score": len(sentences)
    }

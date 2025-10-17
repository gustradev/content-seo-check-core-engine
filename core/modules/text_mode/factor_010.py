import re
def check(content):
    sentences = re.split(r'[.!?]+', content)
    sentences = [s for s in sentences if s.strip()]
    words = content.split()
    avg_len = len(words)/max(len(sentences),1)
    return {
        "factor": "Average Sentence Length",
        "score": round(avg_len,2)
    }

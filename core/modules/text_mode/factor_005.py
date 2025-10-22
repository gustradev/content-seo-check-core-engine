import re

def check(content: str):
    sentences = re.split(r'[.!?]+', content)
    sentences = [s.strip() for s in sentences if s.strip()]
    words = content.split()
    avg_sentence_len = len(words) / len(sentences) if sentences else 0
    return {
        "factor": "Average Sentence Length",
        "value": round(avg_sentence_len, 2)
    }

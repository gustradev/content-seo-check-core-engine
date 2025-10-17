import re
def check(content):
    words = content.split()
    sentences = re.split(r'[.!?]+', content)
    sentences = [s for s in sentences if s.strip()]
    syllables = sum(len(re.findall(r'[aeiouy]+', w.lower())) for w in words)
    score = 206.835 - 1.015 * (len(words)/max(len(sentences),1)) - 84.6 * (syllables/max(len(words),1))
    return {
        "factor": "Flesch Reading Ease",
        "score": round(score, 2)
    }

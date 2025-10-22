import re

def count_syllables(word):
    word = word.lower()
    vowels = "aeiouy"
    count = 0
    prev_char_was_vowel = False
    for char in word:
        if char in vowels:
            if not prev_char_was_vowel:
                count += 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    if word.endswith("e"):
        count = max(1, count - 1)
    return count or 1

def check(content: str):
    sentences = re.split(r'[.!?]+', content)
    sentences = [s.strip() for s in sentences if s.strip()]
    words = re.findall(r'\b\w+\b', content)
    syllables = sum(count_syllables(w) for w in words)

    total_sentences = len(sentences)
    total_words = len(words)

    if total_sentences == 0 or total_words == 0:
        score = 0
    else:
        score = 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (syllables / total_words)

    return {
        "factor": "Flesch Reading Ease",
        "value": round(score, 2)
    }

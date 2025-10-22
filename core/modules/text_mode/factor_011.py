import textstat

def check(content):
    value = textstat.flesch_kincaid_grade(content)
    return {
        "factor": "Flesch-Kincaid Grade",
        "value": round(value, 2)
    }

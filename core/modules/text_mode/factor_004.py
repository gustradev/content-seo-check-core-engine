def check(content):
    words = content.lower().split()
    keyword = "seo"
    count = words.count(keyword)
    density = count / max(len(words), 1) * 100
    return {
        "factor": "Keyword Density (seo)",
        "score": round(density, 2)
    }

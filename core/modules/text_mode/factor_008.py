import re
def check(content):
    urls = re.findall(r'https?://\S+', content)
    return {
        "factor": "Number of Links",
        "score": len(urls)
    }

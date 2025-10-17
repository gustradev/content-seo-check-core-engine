from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_text = soup.get_text()
    words = body_text.split()
    return {
        "factor": "Body Word Count",
        "score": len(words)
    }

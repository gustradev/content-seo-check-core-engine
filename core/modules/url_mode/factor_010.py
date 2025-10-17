from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, 'html.parser')
    strong_tags = soup.find_all('strong')
    return {
        "factor": "Bold Text Count (<strong>)",
        "score": len(strong_tags)
    }

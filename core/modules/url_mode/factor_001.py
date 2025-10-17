from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, 'html.parser')
    h1_count = len(soup.find_all('h1'))
    return {
        "factor": "H1 Tag Count",
        "score": h1_count
    }

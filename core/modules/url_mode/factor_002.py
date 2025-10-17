from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, 'html.parser')
    h2_count = len(soup.find_all('h2'))
    return {
        "factor": "H2 Tag Count",
        "score": h2_count
    }

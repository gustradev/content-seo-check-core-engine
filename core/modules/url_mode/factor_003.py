from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    return {
        "factor": "Number of Links",
        "score": len(links)
    }

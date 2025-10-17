from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/')]
    return {
        "factor": "Internal Link Count",
        "score": len(links)
    }

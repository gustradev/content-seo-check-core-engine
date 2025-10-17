from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, 'html.parser')
    desc = soup.find('meta', attrs={'name':'description'})
    return {
        "factor": "Meta Description Present",
        "score": 1 if desc else 0
    }

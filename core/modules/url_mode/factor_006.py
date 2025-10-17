from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string if soup.title else ""
    return {
        "factor": "Title Length",
        "score": len(title)
    }

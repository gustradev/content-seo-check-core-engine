from bs4 import BeautifulSoup

def check(html):
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img')
    return {
        "factor": "Number of Images",
        "score": len(images)
    }

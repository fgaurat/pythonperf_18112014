import requests
from bs4 import BeautifulSoup
import time

def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_log_href = [a['href'] for a in soup.find_all('a') if a["href"].endswith('.log')]

    for href in all_log_href:
        full_url = f"{url}{href}"
        response = requests.get(full_url)
        with open(href,'w') as f:
            f.write(response.text)
    
    end = time.perf_counter()         
    print(f"{end-start:.3f}s")

if __name__=='__main__':
    main()

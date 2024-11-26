import requests
from bs4 import BeautifulSoup
import time
import threading


def download_and_save(url,log_file):
    full_url = f"{url}{log_file}"
    response = requests.get(full_url)
    with open(log_file,'w') as f:
        f.write(response.text)

def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_log_href = [a['href'] for a in soup.find_all('a') if a["href"].endswith('.log')]

    ths = []
    for href in all_log_href:
        th = threading.Thread(target=download_and_save,args=(url,href))
        th.start()
        ths.append(th)

    [th.join() for th in ths]
    end = time.perf_counter()         
    print(f"{end-start:.3f}s")

if __name__=='__main__':
    main()

import requests
from bs4 import BeautifulSoup
import time
import concurrent.futures


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
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_and_save,[url]*len(all_log_href),all_log_href)







    end = time.perf_counter()         
    print(f"{end-start:.3f}s")

if __name__=='__main__':
    main()

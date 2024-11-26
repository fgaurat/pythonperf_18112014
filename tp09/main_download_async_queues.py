import requests
from bs4 import BeautifulSoup
import time
import concurrent.futures
import asyncio
import aiohttp


async def download_and_save_aiohttp(url,log_file):
    full_url = f"{url}{log_file}"
    async with aiohttp.ClientSession() as session:
        async with session.get(full_url) as response:
            content = await response.text()
            with open(log_file,'w') as f:
                f.write(content)

async def download_and_save_requests(url,log_file):
    full_url = f"{url}{log_file}"

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, requests.get, full_url)

    with open(log_file,'w') as f:
        f.write(response.text)


async def download(q_download:asyncio.Queue,q_save:asyncio.Queue):
    pass

async def save(q_save:asyncio.Queue):
    pass



async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all = []
    all_log_href = [a['href'] for a in soup.find_all('a') if a["href"].endswith('.log')]

    for href in all_log_href:
        all.append(download_and_save_aiohttp(url,href))

    r = await asyncio.gather(*all)

    end = time.perf_counter()         
    print(f"{end-start:.3f}s")

if __name__=='__main__':
    asyncio.run(main())
    

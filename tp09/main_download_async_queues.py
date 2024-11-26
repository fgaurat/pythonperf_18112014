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
    while True:
        url,log_file = await q_download.get()
        full_url = f"{url}{log_file}"
        async with aiohttp.ClientSession() as session:
            async with session.get(full_url) as response:
                content = await response.text()
                dict_message = {
                    'log_file':log_file,
                    'content':content
                }
                q_save.put_nowait(dict_message)
        q_download.task_done()
        

async def save(q_save:asyncio.Queue):
    while True:
        d = await q_save.get()
        log_file = d['log_file']
        content = d['content']
        with open(log_file,'w') as f:
            f.write(content)
        q_save.task_done()




async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"

    queue_download = asyncio.Queue()    
    queue_save = asyncio.Queue()    

    nb_download_workers = 10
    nb_save_workers = 5

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all = []
    all_log_href = [a['href'] for a in soup.find_all('a') if a["href"].endswith('.log')]

    tasks = []

    for i in range(nb_download_workers):
        t = asyncio.create_task(download(queue_download,queue_save))
        tasks.append(t)

    for i in range(nb_save_workers):
        t = asyncio.create_task(save(queue_save))
        tasks.append(t)

    for href in all_log_href:
        t = url ,href
        queue_download.put_nowait(t)


    end = time.perf_counter()         
    print(f"{end-start:.3f}s")

if __name__=='__main__':
    asyncio.run(main())
    

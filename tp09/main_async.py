import asyncio
import time
import threading

async def add(a,b):
    print(threading.currentThread().name)
    await asyncio.sleep(1)
    return a+b

async def main():
    start = time.perf_counter()  
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')

    # c = await add(2,3)
    # print(c)

    # c = await add(2,3)
    # print(c)

    l = [add(2,3),add(4,3),add(2,5),add(2,18)]

    r = await asyncio.gather(*l)
    print(r)
    end = time.perf_counter()         
    print(f"{end-start:.3f}s")

if __name__=='__main__':
    asyncio.run(main())


# import time
# def main():
#     print('Hello ...')
#     time.sleep(1)
#     print('... World!')

# if __name__=='__main__':
#     main()

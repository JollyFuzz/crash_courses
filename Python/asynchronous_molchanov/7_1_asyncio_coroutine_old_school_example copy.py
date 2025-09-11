"""
Это немного устаревший пример, так писался код на python3.4
"""

import asyncio


@asyncio.coroutine
def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        yield from asyncio.sleep(0.5)


@asyncio.coroutine
def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passes".format(count // 2))
        count += 1
        yield from asyncio.sleep(0.5)


@asyncio.coroutine
def main():
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())

    yield from asyncio.gather(task1, task2)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

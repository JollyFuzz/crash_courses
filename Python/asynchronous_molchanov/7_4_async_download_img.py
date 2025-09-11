"""
Асинхронная загрузка изображений
"""

import asyncio
import os
import random
import time

import aiofiles
import aiohttp


def generate_name():
    name_len = 5
    name_symbols = [chr(random.randint(65, 90)) for i in range(name_len)]
    return "".join(name_symbols)


async def fetch_content(url, session, label):
    async with session.get(url) as response:
        data = await response.read()
        print(f"Task {label}: downloaded data")
        await write_file(data)
        print(f"Task {label}: done")


async def write_file(content):
    filename = generate_name()

    async with aiofiles.open(filename, "wb") as file:
        await file.write(content)

    os.remove(filename)


async def main():
    start_time = time.time()

    url = "https://dummyimage.com/600x400/000/fff"
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(1, 11):
            print(f"Run {i} task")
            fetch_content_tasks = asyncio.create_task(fetch_content(url, session, i))
            tasks.append(fetch_content_tasks)

        await asyncio.gather(*tasks)

    print(time.time() - start_time)


if __name__ == "__main__":
    asyncio.run(main())

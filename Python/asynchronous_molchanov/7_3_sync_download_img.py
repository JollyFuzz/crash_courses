"""
Синхронная загрузка сообщений
"""
import os
import random
import time

import requests


def generate_name():
    name_len = 5
    name_symbols = [chr(random.randint(65, 90)) for i in range(name_len)]
    return "".join(name_symbols)


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    filename = generate_name()

    with open(filename, "wb") as file:
        file.write(response.content)

    os.remove(filename)


def main():
    start_time = time.time()

    url = "https://dummyimage.com/600x400/000/fff"

    for i in range(10):
        print(f"Run {i}")
        write_file(get_file(url))

    print(time.time() - start_time)


if __name__ == "__main__":
    main()

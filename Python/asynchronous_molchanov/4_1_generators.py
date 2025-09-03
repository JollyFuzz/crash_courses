"""Простейший генератор"""
from time import time

def gen(s):
    for i in s:
        yield i


def get_filename():
    while True:
        pattern = "file-{}.jpeg"
        t = int(time())
        yield pattern.format(str(t))

        print("Q")
import asyncio
import inspect


@asyncio.coroutine
def a():
    return "Text"


# Проверяем, что функция a декоратором asyncio.coroutine была превращена в корутину основанную на генераторе
print(inspect.isgeneratorfunction(a))
g = a()
print(next(g))

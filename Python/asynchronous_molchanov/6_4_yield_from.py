def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class BlaBlaExcpetion(Exception):
    ...

# Тут нет инициализирующего декоратора, т.к. генератор будет проинициализирован при помощи yield from
def subgen():
    while True:
        try:
            message = yield
        except BlaBlaExcpetion:
            print("I see your BlaBla")
        except StopIteration:
            break
        else:
            print("......", message)

    return "Returned from subgen()"

@coroutine
def delegator(g):
    result = yield from g
    print(result)


if __name__ == "__main__":
    sg = subgen()
    g = delegator(sg)

    g.send("OK")
    g.throw(BlaBlaExcpetion)
    g.throw(StopIteration)
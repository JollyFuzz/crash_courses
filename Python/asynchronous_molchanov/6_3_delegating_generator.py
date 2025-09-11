def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class BlaBlaExcpetion(Exception): ...


@coroutine
def subgen():
    while True:
        try:
            message = yield
        except BlaBlaExcpetion:
            print("I see your BlaBla")
        else:
            print("......", message)


@coroutine
def delegator(g):
    while True:
        try:
            data = yield
            g.send(data)
        except BlaBlaExcpetion as e:
            g.throw(e)


if __name__ == "__main__":
    sg = subgen()
    g = delegator(sg)

    g.send("OK")
    g.throw(BlaBlaExcpetion)

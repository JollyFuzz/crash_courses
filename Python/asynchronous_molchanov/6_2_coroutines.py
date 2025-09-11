from inspect import getgeneratorstate


def subgen():
    start_message = "Welcome"
    message = yield start_message
    print("Sungen received:", message)


def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)


if __name__ == "__main__":
    g = average()
    print(getgeneratorstate(g))

    g.send(None)
    print(getgeneratorstate(g))

    result = g.send(1)
    print(result)
    print(getgeneratorstate(g))

    result = g.send(13)
    print(result)
    print(getgeneratorstate(g))

    result = g.throw(StopIteration)
    print(result)
    print(getgeneratorstate(g))

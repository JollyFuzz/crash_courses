def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


def subgen():
    start_message = "Welcome"
    message = yield start_message
    print("Sungen received:", message)


@coroutine
def calculate_average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average


if __name__ == "__main__":
    g = calculate_average()

    g.send(1)
    g.send(13)

    try:
        g.throw(StopIteration)
    except StopIteration as e:
        print(f"Average {e.value}")

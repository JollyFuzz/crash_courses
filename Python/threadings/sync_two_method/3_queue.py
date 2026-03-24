
"""
Решение с очередью задач и одним потоком
"""


import threading
import time
import asyncio
import queue

class Sender:
    def __init__(self) -> None:
        self._queue = queue.Queue()
        self._worker_thread = threading.Thread(target=self._worker, daemon=True)
        self._worker_thread.start()

    def _worker(self) -> None:
        while True:
            name = self._queue.get()
            try:
                print(f"{name}: start")
                asyncio.run(asyncio.sleep(3))  # имитация долгого запроса
                print(f"{name}: end")
            finally:
                self._queue.task_done()

    def send(self, name: str) -> None:
        self._queue.put(name)

    def wait_all(self) -> None:
        self._queue.join()

sender = Sender()

def procucer(name: str) -> None:
    sender.send(name)
    print(f"{name} submitted")


t1 = threading.Thread(target=procucer, args=("thread-1",))
t2 = threading.Thread(target=procucer, args=("thread-2",))
t3 = threading.Thread(target=procucer, args=("thread-3",))

threads = [t1, t2, t3]

start = time.time()

for t in threads:
    t.start()

for t in threads:
    t.join()

sender.wait_all()

print(f"Total time: {time.time() - start:.2f} sec")
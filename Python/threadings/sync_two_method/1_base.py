
"""
Постановка задачи
По сути просто запускаем выполенение метода в двух потоках
"""


import threading
import time
import asyncio

class Sender:
    async def send(self, name: str) -> None:
        await self._wait_for_rate_limit()

        print(f"{name}: start")
        await asyncio.sleep(3)  # имитация долгого запроса
        print(f"{name}: end")

    async def _wait_for_rate_limit(self):
        await asyncio.sleep(2)

def worker(sender: Sender, name: str) -> None:
    asyncio.run(sender.send(name))  # <-- запускаем event loop

sender = Sender()

t1 = threading.Thread(target=worker, args=(sender, "thread1"))
t2 = threading.Thread(target=worker, args=(sender, "thread2"))

start = time.time()

t1.start()11
t2.start()

t1.join()
t2.join()

print(f"Total time: {time.time() - start:.2f} sec")
import threading
import requests
import queue

link = "https://docs.python.org"

content_queue = queue.Queue()

def fetch_data(post_id, url):
    response = requests.get(url)
    content_queue.put((post_id, response.content))

threads = []
for i in range(5):
    t = threading.Thread(target=fetch_data, args=(i, link))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print()
"""
Асинхронный код с использованием Callback
https://www.youtube.com/watch?v=ikKGMp4jb_o&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=3&ab_channel=OlegMolchanov
"""
import socket
import selectors

# Получаем дефолтный селектор ОС
selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    # в data передается callback 
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)

def accept_connection(sc):
    client_socket, addr = sc.accept()
    print("Connection from", addr)

    # в data передается callback
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = "Hello world\n".encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()

def event_loop():
    while True:
        events = selector.select() # (key, events)
        for key, _ in events:
            callback = key.data
            callback(key.fileobj) #fileobj мы передавали при регистраци

if __name__ == "__main__":
    server()
    event_loop()
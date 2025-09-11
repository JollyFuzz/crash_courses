"""
Базовый Hello world для сокетов.
Проблема в том, что работа с подключениями синхронная и по сути исполнение застревает на первом цикле, поэтому невозможно подключить больше 1 клиента.

Источник: https://www.youtube.com/watch?v=ZGfv_yRLBiY&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&ab_channel=OlegMolchanov
"""

import socket

server_socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socker.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socker.bind(("localhost", 5000))
server_socker.listen()

while True:
    print("Before .accept()")
    client_socker, addr = server_socker.accept()
    print("Connection from", addr)

    while True:
        print("Before .recv()")
        request = client_socker.recv(4096)

        if not request:
            break
        else:
            response = "Hello world\n".encode()
            client_socker.send(response)

    print("Outside inner while loop")
    client_socker.close()

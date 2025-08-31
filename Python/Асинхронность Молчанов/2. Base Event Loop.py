"""
https://www.youtube.com/watch?v=g6xvW2FOuPw&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=2&ab_channel=OlegMolchanov
"""
import socket

server_socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socker.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socker.bind(('localhost', 5000))
server_socker.listen()

def accept_connection(server_socker):
    while True:
        print("Before .accept()")
        client_socket, addr = server_socker.accept()
        print('Connection from', addr)
        send_message(client_socket)

        client_socket.close()

def send_message(client_socket):
    while True:
        print("Before .recv()")
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = "Hello world\n".encode()
            client_socket.send(response)



if __name__ == "__main__":
    accept_connection(server_socker)
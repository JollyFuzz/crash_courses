"""
Подход, который здесь рассматривается был предложен
David BeasLey на 2015 PyCon
Переведено Игорем Стариковым
"""

import socket
from select import select

tasks = []

# словарь сокетов на чтение и запись
# где ключ - сокет, значение - функция-генератор, его обслуживающая
to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 5001))
    server_socket.listen()

    while True:

        # Прерываем выполнение функции, т.е. прием соединения
        # Пока функция-генератор не будет вызвана явно
        yield ("read", server_socket)
        client_socket, addr = server_socket.accept()  # read

        print("Connection from", addr)
        # В список задач добавляем функцию-генератор для клиента
        tasks.append(client(client_socket))


def client(client_socket):
    while True:

        # Прерываем выполнение функции, т.е. чтение сообщения
        # Пока функция-генератор не будет вызвана явно для продолжения чтения
        yield ("read", client_socket)
        request = client_socket.recv(4096)  # read

        if not request:
            break
        else:
            response = "Hello, \n".encode()

            # Прерываем выполнение функции, т.е. отправку сообщения
            # Пока функция-генератор не будет вызвана явно для продолжения отправки
            # Это прерывание необязательно, можно сразу после чтения отправить ответ
            # Я закомментировала и проверила, будет работать
            # Думаю, что в этом примере это было сделано с демоцелью,
            # т.к. мы разделяяем "потоки" на чтение и запись
            yield ("write", client_socket)
            client_socket.send(response)  # write

    client_socket.close()


def event_loop():
    # Пока у нас непустые список и словрь
    while any([tasks, to_read, to_write]):

        # Пока список задач пустой
        # Пробуем наполнить его
        while not tasks:
            # получеам список сокетов, готовых на запись и чтение
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            # Добавляем функции-генераторы в список задач
            # Получая соотвествующий генератор и словаря по сокету
            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        # Выполняем первую задачу в списке
        try:
            task = tasks.pop(0)

            # Запускаем генератор дальше
            # и получаем сокет и дальнейшее действие
            action, sock = next(task)

            # обновляем словари на чтение и запись
            if action == "read":
                to_read[sock] = task
            elif action == "write":
                to_write[sock] = task
        except StopIteration:
            print("Done")


if __name__ == "__main__":
    tasks.append(server())
    event_loop()

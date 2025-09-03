"""Простая реализация принципа Round Robin"""

def gen1(s):
    for i in s:
        yield i

def gen2(n):
    for i in range(n):
        yield i

my_name = "Vika"
g1 = gen1(my_name)
g2 = gen2(len(my_name))

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    task_name = task.__name__
    
    try:
        task_result = next(task)
        print(task_result)
        tasks.append(task)
    except StopIteration as e:
        print(f"Задача {task_name} завершила свою работу")
    except Exception as e:
        print(f"При выполнении задачи {task_name} возникла проблема")

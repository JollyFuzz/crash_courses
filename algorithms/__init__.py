import sys
import time
from pathlib import Path

local_path = Path(__file__).parent.parent

sys.path.append(str(local_path))

from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort  import insertion_sort

def check_correct(a):
    """Проверка отсортированного массива"""
    if len(a) < 2:
        return True
    
    for i, item in enumerate(range(len(a)-1), start=1):
        prev_item = a[i-1]
        item = a[i]
        if prev_item > item:
            return False
        
    return True
        

test_cases = [
    # Пустой список
    [],
    
    # Однозначный список
    [1],
    
    # Двухэлементный список
    [3, 1],
    
    # Трехэлементный упорядоченный список
    [1, 2, 3],
    
    # Трехэлементный обратный порядок
    [3, 2, 1],
    
    # Повторяющиеся элементы
    [1, 1, 1],

    [1, 2, 3, 2],
    
    # Большее количество элементов
    [5, 8, 3, 1, 6, 4, 2, 7],
    
    # Отрицательные числа
    [-5, -3, -8, -1],
    
    # Смешанные положительные и отрицательные значения
    [-3, 1, 5, -2, 0],
    
    # Флоат числа
    [1.5, 2.3, 0.1, -1.2],
    
    # Большое число элементов
    list(range(100)),   # список чисел от 0 до 99
    
    # Крайне большие и малые значения
    [float('inf'), float('-inf')],
    
    # Случайные строки (алфавитный порядок)
    # ["apple", "banana", "cherry"],
    
    # Строки разных длин
    # ["a", "ab", "abc"],
    
    # Строковые дубликаты
    # ["hello", "world", "hello"],
]

def test_sort_algorith(f):
    for i, case in enumerate(test_cases, start=1):
        start_time = time.time()
        sorted_a = f(case.copy())
        end_time = time.time()

        result = check_correct(sorted_a)

        print(f"{i} - {result} - {(end_time - start_time)} sec - {case} -> {sorted_a}")

if __name__ == "__main__":
    test_sort_algorith(insertion_sort)
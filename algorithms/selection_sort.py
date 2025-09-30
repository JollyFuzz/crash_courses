# https://leetcode.com/problems/sort-an-array/
#11:53
# Реализация сортировки выбором по книге грокаем алгоритмы
class Solution(object):
    def sortArray(self, nums):
        nums = nums[:]
        sorted_nums = []
        while len(nums) != 0:
            min_val = nums[0]
            min_val_i = 0
            for i, num in enumerate(nums):
                if num < min_val:
                    min_val = num
                    min_val_i = i

            sorted_nums.append(nums.pop(min_val_i))
        
        return sorted_nums
    


test_cases = [
    # Тест №1: пустой список
    # [],
    
    # Тест №2: список с одним элементом
    [5],
    
    # Тест №3: список с несколькими элементами в порядке возрастания
    [1, 2, 3, 4, 5],
    
    # Тест №4: список с несколькими элементами в порядке убывания
    [5, 4, 3, 2, 1],
    
    # Тест №5: список с повторяющимися элементами
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
    
    # Тест №6: список с отрицательными числами
    [-5, -4, -3, -2, -1],
    
    # Тест №7: смешанный список положительных и отрицательных чисел
    [-3, 1, -2, 5, 0, -1, 4],
    
    # Тест №8: список с большим количеством элементов
    list(range(100)),
    
    # Тест №9: список с большим количеством одинаковых элементов
    [1]*100,
]

for test_case in test_cases:
    result = Solution().sortArray(test_case)
    assert result == sorted(test_case)

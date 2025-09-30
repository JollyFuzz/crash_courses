# https://leetcode.com/problems/sort-an-array/
#11:53
# Реализация сортировки выбором по книге грокаем алгоритмы
class Solution(object):
    # реализация в лоб
    def sortArray_v1(self, nums):
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] == nums[1], nums[0]


        p_index = len(nums) // 2
        p_value = nums[p_index]

        right_sublist = []
        left_sublist = []
        
        for n in nums[:p_index]:
            if n > p_value:
                right_sublist.append(n)
            else:
                left_sublist.append(n)
        
        for n in nums[p_index+1:]:
            if n > p_value:
                right_sublist.append(n)
            else:
                left_sublist.append(n)
                
                
        return self.sortArray(left_sublist) + [p_value] + self.sortArray(right_sublist)
    
    # классическая быстрая сортировка
    def sortArray(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            # выбираем центральный элемент в качестве опорного
            pivot = arr[len(arr) // 2]
            # формируем три группы: элементы меньше, равные и большие опорного
            less = [x for x in arr if x < pivot]
            equal = [x for x in arr if x == pivot]
            greater = [x for x in arr if x > pivot]
            # рекурсивно сортируем каждую группу и объединяем их
        return self.sortArray(less) + equal + self.sortArray(greater)


test_cases = [
    [5,2,3,1],
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

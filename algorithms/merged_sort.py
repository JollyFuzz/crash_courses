# https://leetcode.com/problems/sort-an-array/
# Реализация сортировки выбором по книге грокаем алгоритмы
class Solution(object):
    # реализация в лоб
    def sortArray(self, nums):
        if len(nums) < 2:
            return nums
        
        midd_i = len(nums) // 2
        sublist1 = self.sortArray(nums[:midd_i])
        sublist2 = self.sortArray(nums[midd_i:])

        # merge
        p1 = 0
        p2 = 0
        merged_list = []
        while p1 < len(sublist1) and p2 < len(sublist2):
            if sublist1[p1] > sublist2[p2]:
                merged_list.append(sublist2[p2])
                p2 += 1
            else:
                merged_list.append(sublist1[p1])
                p1 += 1

        merged_list += sublist1[p1:]
        merged_list += sublist2[p2:]

        return merged_list



            

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

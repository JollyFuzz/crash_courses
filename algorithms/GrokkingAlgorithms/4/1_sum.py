def my_sum(nums):
    if len(nums) == 0:
        return 0
    
    if len(nums) == 1:
        return nums[0]
    
    return nums[0] + my_sum(nums[1:])


print(my_sum([2,4,6]))
def my_max(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        if nums[0] >= nums[1]:
            return nums[0]
        else:
            return nums[1]
        
    left_max = my_max(nums[:len(nums)//2])
    right_max = my_max(nums[len(nums)//2+1:])
    if not left_max: 
        return right_max
    
    if not right_max:
        return left_max
    
    if left_max >= right_max:
        return left_max
    else:
        return right_max


print(my_max([2,4,6]))
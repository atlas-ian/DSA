def sortedArray(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
        
    return True

arr = [1,2,3,4,5,5,6]
print(sortedArray(arr))
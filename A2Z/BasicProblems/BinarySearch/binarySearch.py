def BinarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
 

        if target == nums[mid]:
            return nums[mid]
        elif target < nums[mid]:
            right = nums[mid] - 1
        else:
            left = nums[mid] + 1

    return "not found"

arr = [1,3,5,7,9,11,14]

print(BinarySearch(arr, 9))
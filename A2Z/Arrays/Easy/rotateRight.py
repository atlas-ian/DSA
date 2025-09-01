def reverse_range(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums

    

def rotateArrayByD(nums, d, n):
    n = len(nums)
    d = d % n
    if d == 0:
        return nums 
    reverse_range(nums, 0, n - 1)
    reverse_range(nums, 0, d - 1)
    reverse_range(nums, d, n - 1)
    return nums



if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    d = 3
    n = len(arr)
    print(rotateArrayByD(arr, d, n))
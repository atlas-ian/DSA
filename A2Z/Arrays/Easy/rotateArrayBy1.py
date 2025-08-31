def rotateBy1(nums):
    temp = nums[0]
    for i in range(1, len(nums)):
        nums[i - 1] = nums[i]
    nums[len(nums) - 1] = temp
    return nums

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    print(rotateBy1(arr))
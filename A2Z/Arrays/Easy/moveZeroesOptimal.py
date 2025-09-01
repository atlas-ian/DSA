def moveZeroesOptimal(nums):
    if 0 not in nums:
        return nums
    for i in range(0, len(nums)):
        if nums[i] == 0:
            j = i
            break
    for i in range(j + 1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums


if __name__ == "__main__":
    arr = [1,0,2,0,3,4,0,0]
    print(moveZeroesOptimal(arr))
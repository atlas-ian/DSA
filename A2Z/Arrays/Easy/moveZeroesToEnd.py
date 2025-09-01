def moveZeroesToEnd(nums):
    temp = []

    for i in range(0, len(nums)):
        if nums[i] != 0:
            temp.append(nums[i])
    return temp

if __name__ == "__main__":
    arr = [1,0,2,0,3,4,0,0]
    print(moveZeroesToEnd(arr))
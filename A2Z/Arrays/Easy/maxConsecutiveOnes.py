def maxConsecutiveOnes(nums):
    count = 0
    total = 0
    for i in range(0, len(nums)):
        if nums[i] == 1:
            count += 1
            total = max(count, total)
        else:
            count = 0
    return total

if __name__ == "__main__":
    arr = [0,1,1,1,1,1,2,3,1,1,1,4,1,1,5]
    print(maxConsecutiveOnes(arr))
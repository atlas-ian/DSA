def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            nums[i + 1] = nums[j]
            i += 1
    return i + 1
    



if __name__ == "__main__":
    arr = [1,1,2,2,2,3]
    print(removeDuplicates(arr))
def max_element(nums):

    maxi = nums[0]

    for i in nums:
        maxi = max(maxi, i)

    # return maxi

    hash_map = {}
    for i in nums:
        hash_map[i] = hash_map.get(i, 0) + 1


    for i in nums:
        if hash_map[i] == 1:
            return i
        
    return maxi

if __name__ == "__main__":
    arr = [1,4,5,1,2,2,4,5,6]
    print(max_element(arr))
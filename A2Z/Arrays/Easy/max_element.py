def max_element(nums):

    maxi = nums[0]

    for i in nums:
        maxi = max(maxi, i)

    return maxi

if __name__ == "__main__":
    arr = [1,4,5,1,2,4,5]
    print(max_element(arr))
def subarraySum(nums, k):
        result = []   # to store subarrays

        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j + 1]) == k:
                    count += 1
                    result.append(nums[i:j + 1])
        return count, result

if __name__ == "__main__":
    k = 6
    arr = [1,4,5,1,2,2,4,5,6]

    print(subarraySum(arr, k))
def missing_number(nums, N):
    hash_map = [0] * (N + 1)
    for num in nums:
        hash_map[num] = 1

    for i in range(0, N + 1):
        if hash_map[i] == 0:
            return i
    return -1

if __name__ == "__main__":
    arr = [0,1,2,3,4,5]
    N = 6
    print(missing_number(arr, N))
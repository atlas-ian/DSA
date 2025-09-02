def missing(nums):
    n = max(nums)
    total_sum = n * (n + 1) // 2  # sum of 0..n

    sum_nums = 0
    for i in nums:
        sum_nums += i

    return total_sum - sum_nums

if __name__ == "__main__":
    arr = [1, 2, 4, 5]  # missing number is 3
    print(missing(arr))  # Output: 3

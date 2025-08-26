# def largest(nums):
#     largest = nums[0]
#     for i in nums:
#         if i > largest:
#             largest = i
#     return largest

# arr = [91, 5, 0, 9, 35]
# print(largest(arr))


def largest(nums):
    largest = 0
    for i in nums:
        if i > largest:
            largest = i
    return largest

arr = [41,9,5,3,4,0, 40,50]
print(largest(arr))
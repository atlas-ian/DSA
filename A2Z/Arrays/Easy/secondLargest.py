def largest(nums):
    largest = 0
    for i in nums:
        if i > largest:
            largest = i
    return largest

def secondLargest(nums):
    secondLargest = -1
    largest_num = largest(nums)
    for i in nums:
        if i > secondLargest and i != largest_num:
            secondLargest = i
    return secondLargest


def secondLargestOptimal(nums):
    largest = nums[0]
    secondLargest = -1
    for i in nums:
        if i > largest:
            secondLargest = largest
            largest = i

        elif i < largest and i > secondLargest:
            secondLargest = i

    return secondLargest

def second_smallest(nums):
    smallest = float('inf')
    second = float('inf')
    for i in nums:
        if i < smallest:
            second = smallest
            smallest = i
        elif i < second and i != second:
            second = i
    return second

if __name__ == "__main__":
    arr = [13,19,23,69,65,65,69,70]
    print(second_smallest(arr))
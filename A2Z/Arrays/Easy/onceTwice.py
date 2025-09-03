# number that appear once reamaining all appears twice - Brute force

def onceTwice(nums):
    for i in nums:
        num = i
        count = 0
        for j in nums:
            if j == num:

                count += 1
        if count == 1:
            return num
    
if __name__ == "__main__":
    arr = [1,2,4,5,1,2,4,5,8,8]
    print(onceTwice(arr))

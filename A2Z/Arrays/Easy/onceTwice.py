# Number that appear once reamaining all appears twice - Brute force

def onceTwice(nums):
    for i in nums:
        num = i
        count = 0
        for j in nums:
            if j == num:

                count += 1
        if count == 1:
            return num
        

def onceTwiceOptimal(nums):
    xor = 0
    for i in nums:
        xor = xor ^ i
    return xor
    
if __name__ == "__main__":
    arr = [1,2,4,5,1,4,5,8,8]
    print(onceTwiceOptimal(arr))

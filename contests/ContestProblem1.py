# You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:
# sumOdd: the sum of the first n odd numbers.
# sumEven: the sum of the first n even numbers.
# Return the GCD of sumOdd and sumEven. 
# Example 1:
# Input: n = 4

# Output: 4

# Explanation:

# Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
# Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
# Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.

# Example 2:

# Input: n = 5

# Output: 5

# Explanation:

# Sum of the first 5 odd numbers sumOdd = 1 + 3 + 5 + 7 + 9 = 25
# Sum of the first 5 even numbers sumEven = 2 + 4 + 6 + 8 + 10 = 30
# Hence, GCD(sumOdd, sumEven) = GCD(25, 30) = 5.

#  

# Constraints:

# 1 <= n <= 10​​​​​​​00

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.

def sumOdd(n):
    odd_sum = 0

    for i in range(n):

        odd_sum += 2 * i + 1
    return odd_sum

def sumEven(n):
    even_sum = 0

    for i in range(n):

        even_sum += 2 * (i + 1)
    return even_sum

def GCD(odd_sum, even_sum):
    while even_sum != 0:
        odd_sum, even_sum = even_sum, odd_sum % even_sum
    return odd_sum

if __name__ == "__main__":
    n = int(input())
    odd_sum = sumOdd(n)
    even_sum = sumEven(n)

    print(sumOdd(n))
    print(sumEven(n))
    print(GCD(odd_sum, even_sum))
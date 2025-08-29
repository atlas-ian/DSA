def sumOfDigits(n):
    sum = 0
    while n != 0:
        last = n % 10
        sum += last
        n //= 10
    return sum


#using recursion

def sumOfDigits1(n):

    if n == 0:
        return 0
    return n % 10 + sumOfDigits1(n // 10)


if __name__ == "__main__":
    n = 123456
    # print(sumOfDigits(n))
    print(sumOfDigits1(n))
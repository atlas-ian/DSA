# the problem is you want to find the sum of the first odd numbers
#for example n = 4, 1 + 3 + 5 + 7 = 16

def sumOdd(n):
    sum = 0

    for i in range(n):

        sum += 2 * i + 1
    return sum


if __name__ == "__main__":
    n = int(input())

    print(sumOdd(n))
    # print(sumEven(n))


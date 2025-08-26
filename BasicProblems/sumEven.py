# the problem is you want to find the sum of the first even numbers
#for example n = 4, 0 + 2 + 4 + 6 = 16

def sumEven(n):
    sum = 0

    for i in range(n):

        sum += 2 * (i + 1)
    return sum


if __name__ == "__main__":
    n = int(input())

    print(sumEven(n))
    # print(sumEven(n))


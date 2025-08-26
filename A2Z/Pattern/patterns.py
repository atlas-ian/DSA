# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
#pattern 1

def pattern1(n):
    
    for i in range(n):
        for j in range(n):
            print("* ", end = '')

        print()

def pattern2(n):

    for i in range(n):
        for j in range(i):
            print("* ", end = "")
        print()

def pattern3(n):

    for i in range(n):
        for j in range(1, i + 1):
            print(j, end = "")
        print()

def pattern4(n):

    for i in range(n):
        for j in range(i):
            print(i, end = "")
        print()

def pattern5(n):
    
    for i in range(n):
        for j in range(n - i + 1):
            print("* ", end = "")           

        print()

def pattern6(n):
    
    for i in range(n):
        for j in range(1, n - i + 1):
            print(j, end = "")           

        print()

def pattern7(n):

    for i in range(n):
        # spaces
        for j in range(2 * i + 1):
            print(" ", end = "")
        # stars
        for j in range(n - i - 1):
            print("*", end = "")

        # spaces
        for j in range(2 * i - 1):
            print(" ", end = "")

        print()


if __name__ == "__main__":
    t = int(input("enter t: "))
    nums = [int(input()) for _ in range(t)]
    for n in nums:
        pattern7(n)
        print()
    
    # print(pattern1(9))




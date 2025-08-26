# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = []
    for i in range(x + 1):
        for j in range(x + 1):
            for k in range(x + 1):
                if i + j + k != n:
                    result.append([i, j, k])

    print(result)

    
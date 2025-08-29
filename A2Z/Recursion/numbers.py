count = 0
def numbers():
    global count
    if count == 4:
        return
    print(count)
    count += 1
    numbers()




    # print linearly from 1 to N
def sequence(i, n):
     
    if i > n:
        return
    print(i)
    sequence(i + 1, n)

if __name__ == "__main__":
    n = int(input())
    sequence(1, n)
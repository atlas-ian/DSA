count = 0
def numbers():
    global count
    if count == 4:
        return
    print(count)
    count += 1
    numbers()

if __name__ == "__main__":

    numbers()
names = 0
def names5():
    global names
    if names == 5:
        return
    print("Atlas")
    names += 1
    names5()

if __name__ == "__main__":

    names5()    
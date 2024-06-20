def screening(a):
    if a % 3 == 0:
        print(" foo", end='')
    if a % 5 == 0:
        print(" bar", end='')
    if a % 7 == 0:
        print(" baz", end='')

if __name__ == '__main__':
    i = 0
    while i < 50:
        i = i + 1
        print(i,".", sep = '', end = '')
        screening(i)
        print("")
    print("конец")
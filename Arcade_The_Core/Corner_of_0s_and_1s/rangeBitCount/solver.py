def rangeBitCount(a, b):

    s = 0
    for n in range(a, b+1):
        s += str(bin(n)).count('1')

    return s

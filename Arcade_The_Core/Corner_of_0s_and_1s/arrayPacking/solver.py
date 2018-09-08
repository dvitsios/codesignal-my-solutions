def arrayPacking(a):

    res = 0
    for i in range(len(a)):

        b = a[i]

        b = b << 8 * i

        res = res | b

    return res

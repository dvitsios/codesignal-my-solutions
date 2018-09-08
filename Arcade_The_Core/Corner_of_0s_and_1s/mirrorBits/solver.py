def mirrorBits(a):

    s = str(bin(a)).replace('0b', '')

    return int(s[::-1], 2)

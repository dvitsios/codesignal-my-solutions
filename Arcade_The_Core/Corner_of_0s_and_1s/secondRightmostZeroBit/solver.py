def secondRightmostZeroBit(n):
    return 2**([m.start() for m in re.finditer(r"0", str(bin(n))[::-1][:-2])][1])

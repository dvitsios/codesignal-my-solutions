def swapAdjacentBits(n):
    return int(''.join([str(bin(n))[::-1][i:i+2].replace('b','0') for i in range(0, len(str(bin(n)))-2, 2)][::-1]), 2)


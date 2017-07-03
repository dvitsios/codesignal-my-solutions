def isCryptSolution(crypt, solution):
    # a + b = c
    a = crypt[0]
    b = crypt[1]
    c = crypt[2]
    ch_dict = {}

    for s in solution:
        ch_dict[s[0]] = int(s[1])

    hasLeadingZeros = False
    if ch_dict[a[0]] == 0 or ch_dict[b[0]] == 0 or ch_dict[c[0]] == 0:
        hasLeadingZeros = True

    n1 = ''.join([str(ch_dict[i]) for i in a])
    n2 = ''.join([str(ch_dict[i]) for i in b])
    n3 = ''.join([str(ch_dict[i]) for i in c])

    if int(n1) + int(n2) == int(n3):
        if hasLeadingZeros and int(n3) == 0 and len(n3) == len(str(int(n3))):
            return True
        elif hasLeadingZeros:
            return False
        else:
            return True
    else:
        return False

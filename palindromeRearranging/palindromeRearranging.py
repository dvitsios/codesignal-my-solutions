def palindromeRearranging(inputString):

    char_occur = {}
    
    for c in inputString:
        if c not in char_occur:
            char_occur[c] = 1
        else:
            char_occur[c] += 1

    odd_occ = [l for l in char_occur if char_occur[l] % 2]
    if len(odd_occ) > 1:
        return False
    else:
        return True
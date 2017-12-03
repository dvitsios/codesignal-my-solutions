def climbingStairs(n, d={}, ways = 0):

    steps = [1, 2] 
      
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    if n in d:
        ways += d[n]
    else:
        ways += climbingStairs(n-1, d, ways) + climbingStairs(n-2, d, ways)
        d[n] = ways

    return ways
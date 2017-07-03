def phoneCall(min1, min2_10, min11, s):

    minutes = 0

    rate = min1
    while s > 0:
        
        minutes += 1
        
        if minutes == 2:
            rate = min2_10
        elif minutes > 10:
            rate = min11
        
        s -= rate
        if s < 0:
            minutes -= 1
        
    return minutes
def avoidObstacles(inputArray):

    for i in range(1, max(inputArray)):
        divs = any([x for x in inputArray if not x%i])
        if not divs:
            return i
    
    return max(inputArray) + 1
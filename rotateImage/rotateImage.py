def rotateImage(a):

    a = list(zip(*a))    
    a = [list(l[::-1]) for l in a]
    
    return a
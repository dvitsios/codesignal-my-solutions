def shapeArea(n):
    
    area = 1
    
    for i in xrange(2, n+1): 
        area += (i-1)*4
                
    return area
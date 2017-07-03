def findAdjacentCells(i,j, n, m):
    l = []
    
    if i > 0:
        l += [(i-1, j)]
        
    if i < (n-1):
        l += [(i+1, j)]
        
    if j > 0:
        l += [(i, j-1)]
        
    if j < m - 1:
        l += [(i, j+1)]
        
    return l

def findPath(matrix):

    starti = -1
    startj = -1
    
    found = False
    for i in range(len(matrix)):
        if found:
            break
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                starti, startj = i, j
                found = True
                break
                
    valid = True
    
    n = len(matrix)
    m = len(matrix[0])
    
    
    for i in range(1, n*m):
        l = findAdjacentCells(starti, startj, n, m)
        print(l)
        
        found_next = False
        for x, y in l:
            if matrix[x][y] == i+1:
                found_next = True
                starti, startj = x, y
                break
        
        if not found_next:
            valid = False
            break
            
    return valid
            
          
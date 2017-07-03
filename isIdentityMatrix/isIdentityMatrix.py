def isIdentityMatrix(matrix):
    flag = True
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if i == j:
                if matrix[i][j] != 1:
                    return False
            elif matrix[i][j] != 0:
                return False
    
    return flag

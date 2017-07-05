def get_adjacent_cells(i, j, m, n):

    coords = []
    if i >= 1:
        if j >= 1:
            coords += [[i-1, j-1]]
        coords += [[i-1, j]]
        
        if j < n - 1:
            coords += [[i-1, j+1]]
                  
    if i < m - 1:
        if j >= 1:
            coords += [[i+1, j-1]]
        coords += [[i+1, j]]
        
        if j < n -1:
            coords += [[i+1, j+1]]
    
    if j >= 1:
        coords += [[i, j-1]]

    if j < n - 1:
        coords += [[i, j+1]]

    return coords


def minesweeper(matrix):

    m = len(matrix)
    n = len(matrix[0])

    num_matrix = [ [0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j]:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
                
    for i in range(m):
        for j in range(n):
                
            coords = get_adjacent_cells(i, j, m, n)
            cur_sum = sum([ matrix[x][y] for (x,y) in coords ])
            num_matrix[i][j] = cur_sum
                
    return num_matrix
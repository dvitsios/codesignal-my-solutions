def line_is_valid(row):
    
    tmp_dict = {}    
    valid = True
    
    if len(row) > 0:
        #print(row)
        for r in row:
            if r in tmp_dict:
                tmp_dict[r] += 1
            else:
                tmp_dict[r] = 1
        
        if tmp_dict[max(tmp_dict, key=tmp_dict.get)] > 1:
            valid = False
    
    return valid
                

def grid_is_valid(grid):
    
    valid = True
    
    for i in range(len(grid)):       
        row = [int(x) for x in grid[i] if x != '.']
        #print(row)
        valid = line_is_valid(row)
        if not valid:
            break
                
    return valid

def sudoku2(grid):
    
    result = False
    
    # check rows:
    rows_valid = grid_is_valid(grid)
        
    # check columns:
    col_valid = grid_is_valid(list(zip(*grid)))
          
    # check 3x3 grids:
    grid3x3_valid = True
    for i in range(0,len(grid), 3):
        
        if not grid3x3_valid:
                break
                
        sub_mat = grid[i:i+3]
        
        for j in range(0,len(grid[0]),3):
            
            tmp_list = [x[j:j+3] for x in sub_mat]
            #print(tmp_list)
            tmp_list = [tmp_list[k][l] for k in range(len(tmp_list)) for l in range(len(tmp_list[k]))]
            
            row = [int(x) for x in tmp_list if x != '.']
            grid3x3_valid = line_is_valid(row)
            #print(grid3x3_valid)
            
            if not grid3x3_valid:
                break
        
            
    if rows_valid and col_valid and grid3x3_valid:
        result = True
        
    return result
def arrayChange(inputArray):

    moves = 0
    
    for i in range(len(inputArray)-1):
        
        left = inputArray[i]
        right = inputArray[i+1]
              
        if left >= right:
            tmp_moves = left - right + 1
            inputArray[i+1] += tmp_moves
            moves += tmp_moves
        
    return moves
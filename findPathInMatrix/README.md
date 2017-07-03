You are given an `n × m` matrix, which contains all the integers from `1` to `n * m`, inclusive, each exactly once.

Initially you are standing in the cell containing the number `1`. On each turn you are allowed to move to an adjacent cell, i.e. to a cell that shares a common side with the one you are standing on now. It is prohibited to visit any cell more than once.

Check if it is possible to visit all the cells of the matrix in the order of increasing numbers in the cells, i.e. get to the cell with the number `2` on the first turn, then move to `3`, etc.

**Example**

* For
```   
    matrix = [[1, 4, 5], 
             [2, 3, 6]]
```

the output should be

`findPath(matrix) = true`

* For
```
    matrix = [[1, 3, 6], 
              [2, 4, 5]]
```

the output should be
`findPath(matrix) = false`.

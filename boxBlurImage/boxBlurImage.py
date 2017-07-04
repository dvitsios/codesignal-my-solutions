def boxBlur(image):

    m = len(image)-2
    n = len(image[0])-2
    blur_img = [ [0] * n for _ in range(m)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            
            indexes = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
            
            avg = int(math.floor(sum([image[k][l]  for (k,l) in indexes]) / 9)) 
            blur_img[i-1][j-1] = avg
            
    return blur_img
def areSimilar(a, b):
 
    left = None
    right = None
   
    areSimilar = True
    
    mism = 0
    for i in range(len(a)):
        
        if a[i] != b[i]:
            mism += 1
        else:
            continue
            
        if mism == 1:
            left = a[i]
            right = b[i]
        elif mism == 2:
            if left == b[i] and right == a[i]:
                continue
            else:
                return False
        elif mism > 2:
            areSimilar = False
            break
    
    return areSimilar


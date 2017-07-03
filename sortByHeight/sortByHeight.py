def sortByHeight(a):

    t = [i for i in range(len(a)) if a[i] == -1]
    persons = list( set(range(len(a))) - set(t) )
      
    p_arr = [ a[i] for i in persons]
    p_arr.sort()
    
    cnt = 0
    for i in persons:
        a[i] = p_arr[cnt]
        cnt += 1
        
    return a
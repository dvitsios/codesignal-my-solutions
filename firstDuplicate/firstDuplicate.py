def firstDuplicate(a):

    dict = {}
    found = 0
    
    for i in range(len(a)):
        if a[i] in dict:
            dict[a[i]] += 1
        else:
            dict[a[i]] = 1
        
        if(dict[a[i]] == 2):
            found = 1
            return a[i]
        
    if not found:
        return -1
       
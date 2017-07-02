def firstNotRepeatingCharacter(s):
    
    occ_dict = {}
    index_dict = {}
    
    for i in range(len(s)):
        
        ch = s[i]
        
        if ch in occ_dict:
            occ_dict[ch] += 1
        else:
            occ_dict[ch] = 1
            
        if ch not in index_dict:
            index_dict[ch] = i


    one_occ = [k for (k,v) in occ_dict.items() if v == 1]
    if len(one_occ) < 1:
        return '_'
    
    index_dict = dict([(k,v) for (k,v) in index_dict.items() if k in one_occ])
    min_ch = min(index_dict, key= index_dict.get)
    
    return min_ch

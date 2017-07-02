def proCategorization(pros, preferences):
        
    pref_dict = {}
    for i in range(len(pros)):
        
        name = pros[i]
        
        prefs = preferences[i]
        for j in range(len(prefs)):
            p = prefs[j]
                
            if p not in pref_dict:
                pref_dict[p] = [name]
            else:
                pref_dict[p] += [name]
                
    
    out_list = []
    
    for k in sorted(pref_dict):
        tmp = [[k], pref_dict[k]]
        out_list += [tmp]
        
    return out_list
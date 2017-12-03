def groupingDishes(dishes):

    d = {}
    
    for l in dishes:
        dish = l[0]
        for i in l[1:]:
            if i not in d:
                d[i] = [dish]
            else:
                d[i] += [dish]
                
    print(d)
    
    out = []
    
    for i in sorted(d):
        if len(d[i]) > 1:
            out += [[i] + sorted(d[i])]
            
    return out
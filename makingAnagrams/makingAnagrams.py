def number_needed(a, b):

    def absol(a):
        if a >= 0:
            return a
        else:
            return (-1)*a

    char_to_del = 0
    
    a_dict = {}
    b_dict = {}
    
    for ch_a in a:
        if ch_a not in a_dict:
            a_dict[ch_a] = 1
        else:
            a_dict[ch_a] += 1
    
    
    for ch_b in b:
        if ch_b not in b_dict:
            b_dict[ch_b] = 1
        else:
            b_dict[ch_b] += 1
    
    all_chars = list(set(list(a_dict.keys()) + list(b_dict.keys())))
    
    for c in all_chars:
        if c not in a_dict:
            a_dict[c] = 0
        if c not in b_dict:
            b_dict[c] = 0
            
    for c in all_chars:
        a_ch = int(a_dict[c]) 
        b_ch = int(b_dict[c])
        #print(a_ch, b_ch)
        diff = a_ch - b_ch
        if diff < 0:
            diff *= -1
        char_to_del += diff
        #print(c, '-', a_dict[c], '-', b_dict[c])
        
    return char_to_del
    
a = input().strip()
b = input().strip()

print(number_needed(a, b))

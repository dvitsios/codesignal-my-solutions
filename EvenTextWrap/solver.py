import textwrap

def textJustification(words, l):
    
    s = ' '.join(words)
    lines = textwrap.wrap(s, l, break_long_words=False)
    
    if len(lines) == 0:
        return [' '* l]
    elif len(lines) == 1:
        return [lines[0] + ' '*(l - len(lines[0]))]
        
    out = []    
    for i in range(len(lines)-1):
        
        w = lines[i].split()
        
        diff = l - (len(lines[i]))
        spaces_arr = [1] * (len(w) - 1)
        
        if len(spaces_arr) > 0:
            idx = 0
            while diff > 0:
                idx %=  len(spaces_arr)
                spaces_arr[idx] += 1
                diff -= 1
                idx += 1
        
        st = ''
        for k in range(len(w)-1):
            st += w[k]
            st += ' ' * spaces_arr[k]
        st += w[-1] + ' ' * diff   
        out += [st]
        

    out += [lines[-1] + ' '*(l - len(lines[-1]))]

    return out
def incrementCipher(s, nums):
        
    for ni in nums:
        
        cnt = 1        
        index = ni * cnt - 1
        
        while index < len(s):
                
                incr_idx = ord(s[index]) + 1
                if incr_idx == 123:
                        incr_idx = 97
                new_ch = chr(incr_idx)
                
                s = s[:index] + new_ch + s[index+1:]
                
                cnt += 1
                index = ni * cnt - 1
                
    return s
    
                
        
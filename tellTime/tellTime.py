def tellTime(time_str):

        t = "It's "
        
        h, m = time_str.split(':')
        h = int(h)
        m = int(m)
                
        if (m % 5) >= 3:
                m = (m // 5) * 5 + 5
                if m == 60:
                        m = 0
                        h += 1
        else:
                m = (m // 5) * 5
                
                
        
        dh = {0: 'twelve', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'one'}
        
        dm = {5: 'five', 10: 'ten', 15: 'quarter', 20: 'twenty', 25: 'twenty five', 30: 'half'}
        
        
        if m == 0:
                t += dh[h]+" o'clock"
        elif m < 31:
                h = h % 12
                t += dm[m]+" past "+ dh[h]
        else:
                h += 1
                h = h % 12
                m = 60 - m
                t += dm[m]+" to "+dh[h]
                
                
        return t
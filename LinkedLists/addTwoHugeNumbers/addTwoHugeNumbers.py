# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def get_num(a):
    cnt_a = 1
    a_num = ''
    while a.next != None:
        
        if cnt_a:
            cnt_a = 0        
            a_num += str(a.value)
        else:
            a_num += ('0' * (4 - len(str(a.value)))) + str(a.value)
                      
        a = a.next
    a_num += ('0' * (4 - len(str(a.value)))) + str(a.value)

    return int(a_num)

def addTwoHugeNumbers(a, b):

    a_num = get_num(a)
    b_num = get_num(b)
    #print(a_num)
    #print(b_num)
    
    sm = str(a_num + b_num)
    #print(sm)
    
    ret_list = []
    sm = sm[-1::-1]
    for i in range(0,len(sm), 4):
        num = sm[i:i+4]
        num = int(num[-1::-1])
        
        ret_list += [num]
        
    ret_list = ret_list[-1::-1]
    
    return ret_list
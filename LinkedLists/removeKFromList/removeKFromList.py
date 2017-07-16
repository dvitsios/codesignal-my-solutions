# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def removeKFromList(head, k):
    
    if head == None:
        return head
    elif head.value == k:
        head = head.next
        
    n = head
     
    while n != None and n.next != None:
        if n.next.value == k:
            n.next = n.next.next
        else:
            n = n.next  
    
    if n != None and n.value == k:
        head = head.next
        
    return head

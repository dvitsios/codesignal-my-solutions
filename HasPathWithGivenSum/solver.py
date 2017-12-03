# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def hasPathWithGivenSum(t, s):

    if t is None:
        if s == 0:
            return 1
        else:
            return 0
    else:
        ans = 0
        subSum = s - t.value

        if subSum == 0 and t.left == None and t.right == None :
                return 1

        if t.left is not None:
            ans = ans or hasPathWithGivenSum(t.left, subSum)

        if t.right is not None:
            ans = ans or hasPathWithGivenSum(t.right, subSum)
        
        return ans
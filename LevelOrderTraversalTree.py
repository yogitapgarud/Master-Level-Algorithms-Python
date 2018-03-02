#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):

    result = []
    
    if t == None:
        return result
    
    queue = []
    queue.append(t)
    
    while queue:
        
        temp = queue.pop(0)
        
        result.append(temp.value)
        
        if temp.left != None:
            queue.append(temp.left)
            
        if temp.right != None:
            queue.append(temp.right)
            
    return result

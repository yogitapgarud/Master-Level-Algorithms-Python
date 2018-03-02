from collections import deque
#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def largestValuesInTreeRows(t):

    result = []
    
    if t == None:
        return result
    
    endnode = Tree('e')
    endnode.value = 'e'
    endnode.left = None
    endnode.right = None
    
    
    queue = deque([])
    queue.append(t)
    queue.append(endnode)
    levelmax = t.value
    
    while queue:
        
        temp = queue.popleft()
        
        if temp.value >= levelmax:
            levelmax = temp.value
            
        if temp.left != None:
            queue.append(temp.left)
            
        if temp.right != None:
            queue.append(temp.right)
            
        if queue and queue[0].value == 'e':
            print("found end")
            result.append(levelmax)
            temp2 = queue.popleft()
            queue.append(endnode)
            levelmax = -2000
 
    return result

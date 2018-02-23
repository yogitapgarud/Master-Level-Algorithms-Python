from heapq import *

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        h = []
        i = 0
        j = 0
        count = k
        result = []
        m = len(matrix)
        n = len(matrix[0])
        indexset = set()
        heappush(h, (matrix[i][j], i, j))
        indexset.add((i,j))
        
        while len(result) < k:
            
            val, i, j = heappop(h)
            result.append(val)
            
            if i+1 < m and (i+1, j) not in indexset:
                heappush(h, (matrix[i+1][j], i+1, j))
                indexset.add((i+1, j))
                
            if j+1 < n and (i, j+1) not in indexset:
                heappush(h, (matrix[i][j+1], i, j+1))
                indexset.add((i, j+1))
            
        return result[k-1]
            
            
            
            
        

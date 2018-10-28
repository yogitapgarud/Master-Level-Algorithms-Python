def minimize(self, A, B, C):
        n = len(A)
        m = len(B)
        l = len(C)
        
        i, j, k = 0, 0, 0
        maxmin = float('inf')
        
        while i < n and j < m and k < l:
            maxmin = min(max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])), maxmin)
            
            if i < n and A[i] <= B[j] and A[i] <= C[k]:
                i += 1
                
            elif j < m and B[j] <= C[k]:
                j += 1
                
            elif k < l:
                k += 1
           
        return maxmin

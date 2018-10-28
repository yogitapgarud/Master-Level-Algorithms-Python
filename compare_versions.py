    def compareVersion(self, A, B):
        A = A.split('.')
        B = B.split('.')
        
        k = len(A)
        m = len(B)
        i = 0
        n = k if k <= m else m
        
        while i < n:
            if int(A[i]) < int(B[i]):
                return -1
                
            elif int(A[i]) > int(B[i]):
                return 1
                
            i += 1
        
        if i < k:
            if int(A[i]) > 0:
                return 1
            
        elif i < m:
            if int(B[i]) > 0:
                return -1
            
        return 0 

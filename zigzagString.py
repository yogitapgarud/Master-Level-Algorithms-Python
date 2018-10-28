def convert(self, A, B):
        
        if B < 2:
            return A
            
        counts = {}
        
        for i in range(B):
            counts[i] = ""
        
        n = len(A)
        row = 0
        
        
        
        for i in range(n):
            counts[row] += A[i]
            if row + 1 == B:
                rev = 1
                row -= 1
            
            elif row - 1 < 0:
                rev = 0
                row += 1
                
            else:
                if rev:
                    row -= 1
                else:
                    row += 1
                    
        ans = ""
        for i in range(B):
            ans += counts[i]
            
        return ans

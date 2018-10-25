def power(self, A):
        n = len(A)
        
        if n == 1 and A[n-1] == '1':
            return 0
            
        num = 0
        
        while n != 1 or A[n-1] != '1':
            
            if int(A[n-1]) % 2 == 1:
                return 0
                
            temp = ''
            
            for i in range(n):
                num = num * 10 + int(A[i])
                if num < 2:
                    if i != 0:
                        temp += '0'
                        
                    continue
                temp += str(num // 2)
                num = num - (num // 2) * 2
            
            A = temp
            n = len(A)
            
        return 1

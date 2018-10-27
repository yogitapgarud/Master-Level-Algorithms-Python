class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        count = 0
        ans = []
        temp = ""
        n = len(A)
        
        for i in range(n):
            c = A[i]
            
            if c == '[' or c == '{':
                if temp and temp[-1] != '\t':
                    ans.append(temp)
                temp = "\t" * count + c
                ans.append(temp)
                count += 1
                temp = "\t" * count
                
            elif c == ']' or c == '}':
                count -= 1
                if temp and temp[-1] != '\t':
                    ans.append(temp)
                temp = "\t" * count + c
                if i < n-1 and A[i+1] != ',':
                    ans.append(temp)
                    temp = "\t" * count
                    
                elif i == n-1:
                    ans.append(temp)
                
            elif c == ',':
                temp += ','
                ans.append(temp)
                temp = "\t" * count
                
            elif c == ' ':
                continue
            
            else:
                temp += c
                
        return ans

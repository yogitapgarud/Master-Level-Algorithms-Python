 def restoreIpAddresses(self, A):
        
        def helper(s, ind, prefix, n, result, count):
            
            if ind == n and count == 4:
                result.append(prefix)
            
            if len(prefix) > 0:
                prefix += "."
                count += 1
            
            ranges = min(n, ind+3)
            for i in range(ind, ranges):
                if int(s[ind:i+1]) < 256:
                    
                    if len(str(int(s[ind:i+1]))) < len(s[ind:i+1]):
                        continue
                    helper(s, i+1, prefix + str(int(s[ind:i+1])), n, result, max(count, 1))
                    
        result = []
        helper(A, 0, "", len(A), result, 0)
        return result

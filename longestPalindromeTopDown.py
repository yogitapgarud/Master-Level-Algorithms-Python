    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def helper(s, i, j):
            if i > j:
                return 0
            
            elif i == j:
                return 1
            
            elif s[i] == s[j]:
                return helper(s, i+1, j-1) + 2
            
            return max(helper(s, i+1, j), helper(s, i, j-1))
        
        return helper(s, 0, len(s)-1)

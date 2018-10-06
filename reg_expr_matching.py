## Contains . or * => '.' matches any single character. '*' matches 0 to n chars.

def check(s1, s2, i, j, m, n):
    
    while i < m and j < n:
        if s1[i] == '.' or s1[i] == s2[j]:
            i += 1
            j += 1
            
        elif s1[i] == '*':
            k = j
            while k < n:
                if check(s1, s2, i+1, k, m, n):
                    return True
                k += 1
            return False
            
        elif s1[i] != s2[j]:
            return False
            
    return True if i == m and j == n else False

s1 = "a*b*cd."
s2 = "aefbhjcde"

print(check(s1, s2, 0, 0, len(s1), len(s2)))

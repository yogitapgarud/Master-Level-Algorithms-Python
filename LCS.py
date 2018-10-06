def LCS(s1, s2, i, j, m, n, mem):
    
    if i == m or j == n:
        return 0
    
    if (i, j) in mem:
        return mem[i,j]
    
    if s1[i] == s2[j]:
        mem[i, j] = 1 + LCS(s1, s2, i+1, j+1, m, n, mem)
    
    else:    
        mem[i, j] = max(LCS(s1, s2, i, j+1, m, n, mem), LCS(s1, s2, i+1, j, m, n, mem))
    
    return mem[i, j]
    
t = int(input())

for _ in range(t):
    lens = input()
    lens = lens.split()
    lens = [int(c) for c in lens]
    
    s1 = input()
    s2 = input()
    
    mem = {}
    print(LCS(s1, s2, 0, 0, len(s1), len(s2), mem))

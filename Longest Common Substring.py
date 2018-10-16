t = int(input())

for _ in range(t):
    lens = input()
    lens = [int(i) for i in lens.split()]
    m, n = lens[0], lens[1]
    
    str1 = input()
    str2 = input()
    
    dp = {}
    dp[-1, -1] = 0
    
    for i in range(m):
        dp[i, -1] = 0
        
    for j in range(n):
        dp[-1, j] = 0
        
    maxsub = 0
    
    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                dp[i, j] = dp[i-1, j-1] + 1
                
            else:
                dp[i, j] = 0
            
            if dp[i, j] > maxsub:
                maxsub = dp[i, j]
                
    print(maxsub)

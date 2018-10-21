t = int(input())

for _ in range(t):
    nums = input().split()
    n, r = int(nums[0]), int(nums[1])
    
    mem = [[0 for i in range(r+1)] for j in range(n+1)]
    
    for i in range(n+1):
        mem[i][0] = 1
        if i < r+1:
            mem[i][i] = 1
    
    for i in range(1, n+1):
        for j in range(1, r+1):
            #print(i, j)
            mem[i][j] = mem[i-1][j-1] + mem[i-1][j]
            
    print(mem[n][r] % (10**9 + 7))

def coin_change(coins, m, n, mem):
    if n == 0:
        return 1
        
    if n < 0:
        return 0
        
    if m < 0:
        return 0
    
    if (m, n) in mem:
        return mem[m, n]
    
    ans = 0
    ans += coin_change(coins, m, n-coins[m], mem)
    ans += coin_change(coins, m-1, n, mem)
        
    mem[m, n] = ans
    
    return ans
    
coins = [1,2,3]
mem = {}
print(coin_change(coins, len(coins)-1, 4, mem))

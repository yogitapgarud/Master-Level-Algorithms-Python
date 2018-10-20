def subset_sum(arr, i, sums, mem):
    if sums == 0:
        return True
        
    if i < 0:
        return False
    
    if (sums, i) in mem:
        return mem[sums, i]
    
    if arr[i] > sums:
        ans = subset_sum(arr, i-1, sums, mem)
        
    else:
        ans = subset_sum(arr, i-1, sums-arr[i], mem) or subset_sum(arr, i-1, sums, mem)
    
    mem[sums, i] = ans
    return ans

arr = [3, 34, 4, 12, 5, 2]
mem = {}
print(subset_sum(arr, len(arr)-1, 0, mem))

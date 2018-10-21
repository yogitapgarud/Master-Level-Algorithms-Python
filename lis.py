def lis(arr, i, state):
    if i < 0:
        return 0
    
    if i in state:
        return state[i]
    
    maxl = 1
    
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i]:
            val = lis(arr, j, state)
            val += 1
            if val > maxl:
                maxl = val
                
    state[i] = maxl
    return maxl

state = {}
arr = [10, 22, 9, 33, 21, 50, 41, 60]
lis(arr, len(arr)-1, state)

maxm = 1

for key, val in state.iteritems():
    if val > maxm:
        maxm = val
        
print(maxm)

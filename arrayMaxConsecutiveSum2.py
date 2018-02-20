def arrayMaxConsecutiveSum2(inputArray):

    l = len(inputArray)
    if l < 1:
        return 0
    
    maxsum = inputArray[0]
    prevsum = maxsum
    
    for i in range(1, l):
        
        currsum = inputArray[i] + prevsum
        
        prevsum = max(currsum, inputArray[i])
            
        maxsum = max(maxsum, prevsum)
            
    return maxsum

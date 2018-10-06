def water(heights, w):
    area = 0
    i = 0
    n = len(heights)
    
    while i < n:
        j = i
        
        while j < n-1 and heights[j] >= heights[j+1]:
            j += 1
            
        while j < n-1 and heights[j] <= heights[j+1]:
            j += 1
                
        minh = min(heights[j], heights[i])
        for k in range(i+1, j):
            if heights[k] < minh: 
                #print(k, heights[k])
                area += w * (minh - heights[k])
                
        
        i = j if i != j else i + 1
        #print("end: ", i, j)
    return area
    
heights = [5,4,1,2,3]
print(water(heights, 1))

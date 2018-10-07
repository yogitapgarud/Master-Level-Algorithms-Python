def smallestWindow(st):
    
    n = len(st)
    
    dic = {}
    setChars = set()
    count = 0
    
    for c in st:
        setChars.add(c)
    
    count = len(setChars)
    
    start = 0
    end = n-1
    curr = 0
    found = set()
    minl = n
    start_ind = 0
    
    for i in range(n):
        c = st[i]
        
        if c in setChars:
            dic[c] = i
            found.add(c)
                
            if len(found) == count:
                while dic[st[start]] > start:
                    start += 1
                
                if i - start + 1 < minl:
                    minl = i - start + 1
                    end = i
                    start_ind = start
            
    return st[start_ind:end+1]
    
st = "aaaabcdabchkdajebcda"
print(smallestWindow(st))

import sys

def minString(str1, str2):
    
    hash1 = {}
    
    hash2 = {}
    
    for s in str2:
        hash2[s] = hash2.get(s, 0) + 1
    
    n2 = len(str2)
    count = 0
    minl = sys.maxint
    end = -1
    start_ind = 0
    start = 0
    
    for i, c in enumerate(str1):
        if c in hash2:
            hash1[c] = hash1.get(c, 0) + 1
            
            if hash1[c] <= hash2[c]:
                count += 1
            
            if count == n2:
                cstart = str1[start]
                while cstart not in hash2 or hash1[cstart] > hash2[cstart]:
                    start += 1
                    if cstart in hash2:
                        hash1[cstart] -= 1
                    cstart = str1[start]
                    
                if i - start + 1 < minl:
                    minl = i - start + 1
                    start_ind = start
                    end = i
                    
    return str1[start_ind:end+1]
    
    
s1 = "zoomlazapzo"
s2 = "oza"
print(minString(s1, s2))

t = int(input())

for _ in range(t):
    n = int(input())
    arr = input().split()
    arr = [int(i) for i in arr]
    
    def comparator(a, b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        return (int(ba) > int(ab)) - (int(ba) < int(ab))
        
    def mycompare(mycmp):
        
        class K(object):
            def __init__(self, obj, *args):
                self.obj = obj
                
            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0
                
            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0
                
            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0
                
            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0
                
            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0
                
            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0
                
        return K
        
    sorted_array = sorted(arr, key=mycompare(comparator)) 
    #print(sorted_array)
    number = "".join([str(i) for i in sorted_array]) 
    print(number) 
    
    """   
    if __name__ == "__main__": 
        a = [54, 546, 548, 60] 
        
    """
        

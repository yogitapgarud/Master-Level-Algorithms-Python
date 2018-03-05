
def nqueens(n):

  result = [(),(),()]
  return addqueen(0, 0, 1)
  
  def addqueen(r, c, i):
  
    if checkqueen(r, c, i):
      result.add(r,c)
      if i == n:
      	return result
      addqueen(0, c+1, i+1)

    else:
      if r+1 == n:
      	check = remove(c-1, i-1)
      
        if check == False:
          return False
      addqueen(r+1, c, i)
      
  def remove(c, i):
    r, c =result.pop()
    
    if r+1 > n and i == 1:
    	return False
    
    addqueen(r+1, c, n)
    
  def checkqueen(r, c, i):
  	
    j = i-2
       
    while j > -1:
    	pr, pc = result[j]
    	if pr == r or pc == c or abs(pr-r) == abs(pc-c):
    		return False
      j -= 1
    
    return True

"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    i=5
    total = len(result)
    while (total <= i):
        #print([i])
        result.append(i)
        i-=1
    return result

r=fn_hack_7() 

print(r)


  
  
    


  
  
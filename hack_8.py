"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
     result = [1,3,5,7,9]
     result.remove(1)
     result.remove(9)
     return result 
    
print(fn_hack_8())




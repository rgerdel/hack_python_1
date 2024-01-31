"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

# def fn_hack_9():
#     result = [1,2,3]
#     #...
#     return result  

def fn_hack_9():
    result = [1,2,3]
    r=[]
    for i, v in enumerate(result):
        r.append(v)
        r.append("@")

    return r
    
r=fn_hack_9() 

print(r)
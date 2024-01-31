"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    
    lista1 =[]
    lista2 = []
    result = "fooziman"
    result = "fooziman".replace("o","0")
    result = result.replace("a","@")
    result = result.replace("i","1")
    result = result.upper()
    
    lista1.append(result)
    lista2 = list(lista1[0])
   
    return lista2  

r=fn_hack_10() 

print(r)
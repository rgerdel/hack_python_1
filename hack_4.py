"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"[0:-1].lower()
    result = result +"fooziman"[-1].upper() 
    return result

print (fn_hack_4())
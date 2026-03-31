a=[9,4,5,6,7,4,3]

def max_min(a):
    q=0
    y=0
    
    for x in a:
        if x > q:
            q=x
        else:
            y=x
            
    return q,y
print(max_min(a))
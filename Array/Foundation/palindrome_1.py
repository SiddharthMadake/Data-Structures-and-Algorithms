a="qwerrewq"

def pal(a):
    l=0
    r=len(a)-1
    while l < r:
        if a[l] != a[r]:
            return False
        l+=1
        r-=1
    return True
    
if pal(a):
    print("pal")
else:
    print("not pal")
        
        
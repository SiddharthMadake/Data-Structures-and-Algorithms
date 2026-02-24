a=[5,3,7,5,2,7,8,2]

def rev(a):
    l=0
    r=len(a)-1
    
    while l < r:
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1
    return a

print(rev(a))
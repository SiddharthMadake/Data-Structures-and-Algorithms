a=[2,4,5,6,74,5,9]

def rev(a):
    l=0
    r=len(a)-1
    while l < r :
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1
    return a

print(rev(a))
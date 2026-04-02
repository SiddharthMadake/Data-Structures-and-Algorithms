a=[1,2,4,5,6,0,-4,-2,-5,9]
a.sort()

def sqr(a):
    l=0
    r=len(a)-1
    pos=len(a)-1
    res=[0]*len(a)
    while l <= r:
        if abs(a[l]) > abs(a[r]):
            res[pos]= a[l] * a[l]
            l+=1
        else:
            res[pos]= a[r] * a[r]
            r-=1
        pos -=1
    return res

print(sqr(a))       
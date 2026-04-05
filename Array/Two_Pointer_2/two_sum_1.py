a=[1,4,5,7,3,2,4]
a.sort()
t=10
c=[]
def two(a,t):
    l=0
    r=len(a)-1
    while l<r:
        s=a[l]+a[r]
        if t == s:
            c.append([a[l],a[r]])
            l+=1
            r-=1
        elif t < s:
            r-=1
        else:
            l+=1
    return c
print(two(a,t))
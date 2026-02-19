a=[-3,-4,-6,0,1,3,4,5]
a.sort()
b=len(a)
c=[]

def three(a):
    
    for i in range(b-2):
        l=i+1
        r=b-1
        while l < r:
            total=a[i]+a[l]+a[r]
            if total == 0:
                c.append([a[i],a[l],a[r]])
                l+=1
                r-=1
            elif total>0:
                r-=1
            else:
                l+=1
    return c
print(three(a))
a=[1,4,6,-3,-1,3,5,-2,0]
a.sort()
b=len(a)
c=[]

def four(a):
    for i in range(1,b-3):
        for j in range(i+1,b-2):
            l=j+1
            r=b-1
            while(l<r):
                t= a[i]+a[j]+a[l]+a[r]
                
                if t == 0 :
                    c.append([a[i],a[j],a[l],a[r]])
                    l+=1
                    r-=1
                elif t > 0:
                    r -=1
                else:
                    l +=1
    return c
print(four(a))
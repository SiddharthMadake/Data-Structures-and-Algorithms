a=[1,2,3,4,5,6,7]
t=12    
def four(a,t):
    a.sort()
    
    c=[]
    for i in range(len(a)-3):
        for j in range(i+1,len(a)-2):
            l=j+1
            r=len(a)-1
            while(l<r):
                s= a[i] + a[j] + a[l] +a[r]
                if s == t:
                    c.append([a[i] ,a[j],a[l],a[r]])
                    l+=1
                    r-=1
                elif s > t:
                    r-=1
                else:
                    l+=1
    return c
print(four(a,t))
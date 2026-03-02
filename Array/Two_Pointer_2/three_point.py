a=[1,3,4,5,2,-1,-4,-3]
a.sort()
c=[]
t=1
def three(a,t):
    
    for i in range(len(a)-2):
        l=i+1
        r=len(a)-1
        s= a[i] + a[l] +a[r]
        while (l < r):
            if s== t:
                c.append([a[i], a[l],a[r]])
                l+=1
                r-=1
            elif s > t:
                r -=1
            else:
                l +=1
    return c

print(three(a,t))
def max_sub(a,k):
    n=len(a)
    w=sum(a[:k])
    w_m=w
    for i in range(k,n):
        w+=a[i]
        w-=a[i-k]
        w_m=max(w,w_m)
        
    return w_m
a=[3,8,6,2,1,5,-4,-7,-9]
k=3
print(max_sub(a,k))
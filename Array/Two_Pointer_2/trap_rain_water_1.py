def trap(a):
    l=0
    r=len(a)-1
    lmax,rmax=0,0
    res=0
    while l < r:
        lmax=max(lmax,a[l])
        rmax=max(rmax,a[r])
        
        if  lmax < rmax :
            res+= lmax - a[l]
            l+=1
        else:
            res+= rmax - a[r]
            r-=1
    return res
a=[4,5,3,6,4,1,8]
print(trap(a))
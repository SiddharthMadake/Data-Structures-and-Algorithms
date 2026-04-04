height=[4,2,3,5,6,3,4]

def trap_a(height):
    a=0
    l=0
    r=len(height)-1
    lmax=0
    rmax=0
    while(l<r):
        lmax=max(lmax,height[l])
        rmax=max(rmax,height[r])
        
        if lmax < rmax:
            a+= lmax - height[l]
            l+=1
        else:
            a+= rmax -height[r]
            r-=1
    return a

print(trap_a(height))
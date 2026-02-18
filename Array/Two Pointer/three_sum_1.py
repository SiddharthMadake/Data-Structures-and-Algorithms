a=[1,4,2,4,6,8,-3,-4,-2,1,0]
a.sort()

def three(a):
    b=len(a)
    c=[]
    
    for i in range(b-2):
        
        left=i+1
        right=b-1
        

        while left < right:
            total=a[i]+a[left]+a[right]
            
            if total == 0:
                c.append([a[i],a[left],a[right]])
                left +=1
                right-=1
                
            elif total > 0:
                right -=1
                
            else:
                left+=1
    return c

print(three(a))             
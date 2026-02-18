def three_sum(n):
    n.sort()
    a=len(n)
    result=[]
    for i in range(a-2):
        
        left = i+1
        right = a-1
        
        while left < right :
            total = n[i] + n[left] + n[right]
            
            if total == 0:
                 result.append([n[i], n[left], n[right]])
                 left+=1
                 right-=1
                
            elif total > 0:
                right -= 1
                
            else:
                left += 1
    return result   
    
s=[1,-2,-1,0,1,3]
#=[-2,-1,0,1,1,3]
print(three_sum(s))
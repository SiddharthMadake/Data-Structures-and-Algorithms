a= [1,3,5,7,8]
c=[]
def two(a):
    left=0
    right=len(a)-1
    
    target=8
    
    while left < right:
         
         sum_1= a[left] + a[right]
         
         if target==sum_1:
            c.append([a[left],a[right]]) 
            left+=1
            right-=1
         elif sum_1 > target :
             right -=1
         else:
             left+=1
    return c
            
print(two(a))
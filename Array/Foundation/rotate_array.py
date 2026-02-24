a=[1,2,3,4,5,6,7]

def r_array(a,k):
    b=len(a) 
    k=k%b
    
    a=a[-k:]+a[:-k]
    
    return a
print(r_array(a,3))
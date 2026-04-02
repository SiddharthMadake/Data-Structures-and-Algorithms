a=[1,2,3,4]
b=[3,5,7]

def merge(a,b):
    i,j=0,0
    res=[]
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    
    while i< len(a):
        res.append(a[i])
        i+=1
        
    while j < len(b):
        res.append(b[j])
        j+=1
    return res
print(merge(a,b))
        
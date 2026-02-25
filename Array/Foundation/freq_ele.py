a=[1,2,5,2,3,6,4,4,1,5,6,3,2,1,3]
a.sort()
frq={}

def feq(a):
    count=0
    for i in a:
        if i in frq:
            frq[i]+=1
            
        else:
            frq[i]=1
    return frq
        
print(feq(a))
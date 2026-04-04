a=[2,5,7,9,6,5]
b=len(a)
prefix= [0] * b
prefix[0]=a[0]

for i in range(1,b):
    prefix[i]= prefix[i-1] + a[i]
    
print(prefix)

def c(f,l):
    if f==0:
        return prefix[l]
    else:
        return prefix[l] - prefix[f-1]
print(c(1,4))
    
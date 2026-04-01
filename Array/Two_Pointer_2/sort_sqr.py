a=[-2,-4,1,4,6,7]
a.sort()

def sort_sqr(a):
    pos=len(a)-1
    result=[0]* len(a)

    l=0
    r=len(a)-1
    while l <= r:
        if abs(a[l])> abs(a[r]):
            result[pos]= a[l] * a[l]
            l +=1
        else:
            result[pos]= a[r] * a[r]
            r -=1
        pos -=1
    return result
print(sort_sqr(a))
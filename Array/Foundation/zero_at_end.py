a=[5,6,0,9,0,3,0,6,4,1,0]
def zero_end(a):
    slow=0
    for fast in range(len(a)-1):
        if a[fast] != 0:
            a[slow],a[fast]=a[fast],a[slow]
            print(a[fast],a[slow],a)
            slow+=1
    return a

print(zero_end(a))
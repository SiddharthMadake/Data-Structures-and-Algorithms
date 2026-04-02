a=[1,0,5,6,0,3,78,9,4,0,3]

def zero_end(a):
    for i in range(len(a)-1):
        if a[i] == 0:
            z=a.replace(a[a[i])
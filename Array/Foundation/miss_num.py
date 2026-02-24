a=[1,2,3,4,5,6,7,9,10]
#8. Find Missing Number (1 to N)
a.sort()

def miss_num(a):
    for i in range(1,len(a)+1):
        if i != a[i-1]:
            print("missing num is", i)
            return
miss_num(a)
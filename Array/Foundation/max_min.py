a=[985,45,6,7,9,89,10]

def max_a(a):
    m=a[0]
    l=a[0]
    for i in range(1,len(a)):
        if a[i] > m:
            m=a[i]
        elif a[i] < l:
            l=a[i]
    return m,l
print(max_a(a))
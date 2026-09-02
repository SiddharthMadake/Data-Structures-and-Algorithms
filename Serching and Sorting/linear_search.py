def linear_search(a):
    f=False
    t=10
    for i in range(len(a)):
        if a[i] == t :
            print("Element found at index",i)
            f=True
            break
    if not f:
        print("element is not present")

a=[1,3,5,6,8,9]
linear_search(a)
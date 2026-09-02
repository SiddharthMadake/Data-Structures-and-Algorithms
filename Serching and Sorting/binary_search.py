def binary_search(a):
    l=0
    r=len(a)-1
    t=7
    while l <= r :
        mid = (l + r) // 2
        if a[mid] == t:
            return mid
            break
        elif a[mid] < t:
            l= mid + 1
        else: 
            r = mid -1
    return -1
print(binary_search([2,5,6,7,8]))
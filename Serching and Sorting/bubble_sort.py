def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
print(bubble_sort([3,6,2,8,5]))
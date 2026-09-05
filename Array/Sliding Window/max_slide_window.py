def max_sum_k(a):
    k=int(input("Enter Sub Array length:"))
    window=sum(a[:k])
    max_window=window
    
    for i in range(k,len(a)):
        window+=a[i]
        window-=a[i-k]
        max_window=max(window,max_window) 
    
    return max_window

a=[1,3,4,5,7,3,9,5,8,5]
print(max_sum_k(a))  
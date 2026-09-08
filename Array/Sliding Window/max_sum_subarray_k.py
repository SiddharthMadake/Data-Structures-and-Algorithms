def max_sum(a,k):
    n =len(a)
    w = sum(a[:k])
    m_w=w
    
    for i in range(k,n):
        w += a[i]
        w-=a[i-k]
        m_w=max(m_w,w)
        
    return m_w

a=[3,6,7,-5,-3,-4,8,9,2]
k=3
print(max_sum(a,k))
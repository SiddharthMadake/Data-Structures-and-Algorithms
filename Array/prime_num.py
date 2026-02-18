def prime(a):
    b = 0
    c = 1 
    
    for i in range(2,a):
        for j in range(2,i):
            if i % j ==0 :
                break
        else:
            print(i)
                
prime(100)
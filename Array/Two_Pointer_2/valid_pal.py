def valid_pal(a):
    l =0
    r=len(a)-1
    
    while l < r:
        
        while l < r and not a[l].isalnum():
            l+=1
            
        while l < r and not a[r].isalnum():
            r-=1
            
        if a[l].lower() != a[r].lower():
            return False
        l+=1
        r-=1
    return True

a="A man, a plan, a canal: Panama"
if valid_pal(a):
    print("valid pal")
else:
    print("not valid")
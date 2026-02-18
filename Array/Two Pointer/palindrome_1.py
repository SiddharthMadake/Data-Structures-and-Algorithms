s="abcddba"

def pal(s):
    left=0
    right=len(s)-1
    
    while left< right:
        if s[left] != s[right]:
            return False 
        left+=1
        right -=1
        
    return True
    
if pal(s):
    print("palindrome")
else:
    print("not palindrome")
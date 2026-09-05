def long_substring(s):
    seen=set()
    left=0
    max_str=0
    
    for right in range(len(s)):
        
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
            
        seen.add(s[right])
        max_str=max(max_str,right-left+1)
        
    return max_str

s="abcfgscde"
print(long_substring(s))
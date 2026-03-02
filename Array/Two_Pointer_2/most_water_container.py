height=[1,3,6,9,3,4]

def water(height):
    l=0
    r=len(height)-1
    max_water=0

    while(l<r):
        w=r-l
        h=min(height[l],height[r])
        area=w*h
        max_water=max(max_water,area)
        if height[l] < height[r]:
            l +=1
        else:
            r -=1
    return max_water

print(water(height))
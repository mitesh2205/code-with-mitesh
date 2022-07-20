import math
piles = [3,4,5,11]
h =8
l,r = 1, max(piles)
        
res = r
while l <= r:
    k = (l + r) // 2
    hours = 0
    for p in piles:
        hours += math.ceil(p / k)
    if hours <= h:
        res = min(res,k)
        r = k-1
    else:
        l = k+1          
print(res)
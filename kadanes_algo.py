# Kadanes algorithm

arr=[-1,-2,-3,-4]
curr=0
maxi=float('-inf')
for i in arr:
    curr+=i
    maxi=max(curr,maxi)
    if curr<0:
        curr=0
print(maxi)
ratings=[1,0,2]
candy = [1]*len(ratings)
        
for i in range (1,len(ratings)):
    if(ratings[i] > ratings[i-1]):
        candy[i] = candy[i-1] + 1
        
if(len(ratings) > 1):
    if(ratings[0] > ratings[1]):
        candy[0] = 2
            
for i in range (len(ratings)-2 , -1, -1):
    if(ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]):
        candy[i] = candy[i+1] + 1
print(sum(candy))
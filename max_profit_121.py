prices = [7,1,5,4,6,2];
i = 0
j = i +1
max = 0
        
while j < len(prices):
    if(prices[j] - prices[i] < 0):
        i = j
        j += 1
            
    else:
        if(prices[j] - prices[i] > max):
            max = prices[j] - prices[i]
        j += 1
            
print(max)
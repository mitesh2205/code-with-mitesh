prices = [7,4,5,3,2,6]
profit = 0
for i in range(len(prices) -1):
    if(prices[i] < prices[i+1]):
        profit += (prices[i+1] - prices[i])
    else:
        continue
print(profit)
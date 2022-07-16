matrix = [[1,2,3],[4,5,6],[7,8,9]]
size = len(matrix) * len(matrix[0])
starting_r = starting_c = 0
ending_r = len(matrix) - 1
ending_c = len(matrix[0])-1
output = []
while(len(output) < size):
    # top left to top right
    for i in range (starting_c,ending_c + 1):
        output.append(matrix[starting_r][i])
    # topright to bottom right 
    for i in range (starting_r + 1,ending_r + 1):
        output.append(matrix[i][ending_c])
    # bottom right to bottom left 
    for i in range (ending_c - 1,starting_c - 1,-1):
        output.append(matrix[ending_r][i])
    # botom left to top left    
    for i in range (ending_r - 1, starting_r, -1):
        output.append(matrix[i][starting_c])

    starting_r += 1
    starting_c += 1
    ending_r -= 1
    ending_c -= 1
        
print(output[:size])
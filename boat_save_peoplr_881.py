people = [1,2]
limit = 3
people.sort()
i = 0
j = len(people) - 1
boat = 0

while (i <= j):
    if(i == j):
        print(boat + 1)

    if(people[j] + people[i] <= limit):
        i +=1
    boat += 1
    j -= 1

print(boat)
candies = [2,3,5,1,3]
extraCandies = 3

for i in range(len(candies)):
    candies[i] = candies[i] + extraCandies

print(candies)

lowest = sorted(candies)[0]
print(lowest)

bool_list =[]

for candy in candies:
    if candy  > lowest:
        bool_list.append('true')

    else:
        bool_list.append('false')

print(bool_list)


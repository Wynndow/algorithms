from random import randint

def closest_pair(input):
    if len(input) <= 3:
        return brute_force_closest_pair(input)



def brute_force_closest_pair(input):
    smallest_distance = float("inf")
    closest_points = None
    for i in range(0, len(input)-1):
        for j in range(i+1, len(input)):
            distance = ((input[j][0] - input[i][0]) ** 2 + (input[j][1] - input[i][1]) ** 2) ** 0.5
            if distance < smallest_distance:
                smallest_distance = distance
                closest_points = (input[i], input[j])
    return closest_points




input = [(x, y) for x, y in zip([randint(0, 100) for x in range(1000)], [randint(0, 100) for y in range(1000)])]
print(brute_force_closest_pair(input))

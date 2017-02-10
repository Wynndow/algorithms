from random import randint

def closest_pair(input_points):
    x_sorted_input_points = sorted(input_points, key=lambda point: point[0])
    y_sorted_input_points = sorted(input_points, key=lambda point: point[1])

    left_closest = recurse_to_smallest_pair(
        x_sorted_input_points[:len(x_sorted_input_points)/2],
        y_sorted_input_points[:len(y_sorted_input_points)/2],
    )
    right_closest = recurse_to_smallest_pair(
        x_sorted_input_points[len(x_sorted_input_points)/2:],
        y_sorted_input_points[len(y_sorted_input_points)/2:],
    )

    smallest_pair_from_halves = min(left_closest, right_closest, key=lambda data: data[2])

    split_closest = calculate_split_closest(
        x_sorted_input_points,
        y_sorted_input_points,
        smallest_pair_from_halves[2],
    )
    print("LEFT: {}\nRIGHT: {}\nSPLIT: {}".format(left_closest, right_closest, split_closest))
    return min(left_closest, right_closest, split_closest, key=lambda data: data[2])
    # print("LEFT: {}    RIGHT: {}".format(left_closest, right_closest))

def calculate_split_closest(x_sorted, y_sorted, delta):
    middle_x = x_sorted[len(x_sorted)/2][0]
    interesting_points = [point for point in y_sorted if point[0] >= middle_x - delta and point[0] <= middle_x + delta]
    smallest_distance = delta
    closest_pair = (None, None, float("inf"))
    print(interesting_points)
    for i in range(0, len(interesting_points)-1):
        for jay in range(1, min(7, len(interesting_points)-i)):
            point_1 = interesting_points[i]
            point_2 = interesting_points[i + jay]
            distance = ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5
            if distance < smallest_distance:
                smallest_distance = distance
                closest_pair = [interesting_points[i], interesting_points[i + jay], distance]
    return closest_pair

def recurse_to_smallest_pair(x_sorted_input_points, y_sorted_input_points):
    if len(x_sorted_input_points) <= 3:
        return brute_force_closest_pair(x_sorted_input_points)

    left_closest = recurse_to_smallest_pair(
        x_sorted_input_points[:len(x_sorted_input_points)/2],
        y_sorted_input_points[:len(y_sorted_input_points)/2],
    )
    right_closest = recurse_to_smallest_pair(
        x_sorted_input_points[len(x_sorted_input_points)/2:],
        y_sorted_input_points[len(y_sorted_input_points)/2:],
    )

    if left_closest[2] < right_closest[2]:
        return left_closest
    else:
        return right_closest

def brute_force_closest_pair(input_points):
    smallest_distance = float("inf")
    closest_pair = None
    for i in range(0, len(input_points)-1):
        for j in range(i+1, len(input_points)):
            distance = ((input_points[j][0] - input_points[i][0]) ** 2 + (input_points[j][1] - input_points[i][1]) ** 2) ** 0.5
            if distance < smallest_distance:
                smallest_distance = distance
                closest_pair = (input_points[i], input_points[j], distance)
    return closest_pair

input_points = [(x, y) for x, y in zip([randint(0, 10) for x in range(10)], [randint(0, 10) for y in range(10)])]
# print(recurse_to_smallest_pair(list(set(input_points))))
print(closest_pair(list(set(input_points))))

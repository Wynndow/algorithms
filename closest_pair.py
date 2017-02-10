import random
from random import randint
from datetime import datetime, timedelta

def closest_pair(input_points):
    x_sorted_points = sorted(input_points, key=lambda point: point[0])
    y_sorted_points = sorted(input_points, key=lambda point: point[1])
    x_sorted_length = len(x_sorted_points)

    left_closest_pair = _recurse_to_closest_pair(
        x_sorted_points[:x_sorted_length/2]
    )
    right_closest_pair = _recurse_to_closest_pair(
        x_sorted_points[x_sorted_length/2:]
    )

    closest_pair_from_halves = min(left_closest_pair, right_closest_pair, key=lambda pair_data: pair_data[2])

    closest_split_pair = _calculate_closest_split_pair(
        x_sorted_points,
        y_sorted_points,
        closest_pair_from_halves[2],
    )
    print("LEFT: {}\nRIGHT: {}\nSPLIT: {}".format(left_closest_pair, right_closest_pair, closest_split_pair))
    return min(left_closest_pair, right_closest_pair, closest_split_pair, key=lambda pair_data: pair_data[2])

def _calculate_closest_split_pair(x_sorted, y_sorted, delta):
    mid_x = x_sorted[len(x_sorted)/2][0]
    potential_closest_split_pairs = [
        point for point in y_sorted
        if point[0] >= mid_x - delta
        and point[0] <= mid_x + delta
    ]
    smallest_distance = delta
    closest_pair = (None, None, float("inf"))
    for i in range(0, len(potential_closest_split_pairs)-1):
        for j in range(1, min(7, len(potential_closest_split_pairs)-i)):
            point_1 = potential_closest_split_pairs[i]
            point_2 = potential_closest_split_pairs[i + j]
            distance = ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5
            if distance < smallest_distance:
                smallest_distance = distance
                closest_pair = [potential_closest_split_pairs[i], potential_closest_split_pairs[i + j], distance]
    return closest_pair

def _recurse_to_closest_pair(x_sorted_points):
    if len(x_sorted_points) <= 3:
        return _brute_force_closest_pair(x_sorted_points)

    left_closest = _recurse_to_closest_pair(
        x_sorted_points[:len(x_sorted_points)/2]
    )
    right_closest = _recurse_to_closest_pair(
        x_sorted_points[len(x_sorted_points)/2:]
    )

    if left_closest[2] < right_closest[2]:
        return left_closest
    else:
        return right_closest

def _brute_force_closest_pair(input_points):
    smallest_distance = float("inf")
    closest_pair = None
    for i in range(0, len(input_points)-1):
        for j in range(i+1, len(input_points)):
            if _distance_between(input_points[i], input_points[j]) < smallest_distance:
                smallest_distance = _distance_between(input_points[i], input_points[j])
                closest_pair = (input_points[i], input_points[j], smallest_distance)
    return closest_pair

def _distance_between(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


random.seed(100)
input_points = [(x, y) for x, y in zip((randint(0, 1000) for x in range(100000000)), (randint(0, 1000) for y in range(100000000)))]

t_start = datetime.now()
print(closest_pair(list(set(input_points))))
t_finish = datetime.now()

taken = t_finish - t_start
print(taken)

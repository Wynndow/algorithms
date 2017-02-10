from random import shuffle
from algorithms.closest_pair import closest_pair

class TestClosestPair():
    def test_closest_pair_and_distance_are_found_for_x_in_first_half(self):
        input_points = [(2, 3), (3, 4), (5, 1), (12, 10), (12, 30), (40, 50)]

        closest_pair_result = closest_pair(input_points)

        assert closest_pair_result[0] == (2, 3)
        assert closest_pair_result[1] == (3, 4)
        assert closest_pair_result[2] == 1.4142135623730951

    def test_closest_pair_and_distance_are_found_for_x_in_second_half(self):
        input_points = [(5, 1), (12, 10), (12, 30), (40, 50), (41, 3), (42, 4)]

        closest_pair_result = closest_pair(input_points)

        assert closest_pair_result[0] == (41, 3)
        assert closest_pair_result[1] == (42, 4)
        assert closest_pair_result[2] == 1.4142135623730951

    def test_closest_pair_and_distance_are_found_for_split_pair(self):
        input_points = [(19, 15), (33, 35), (36, 34), (36, 45), (39, 21), (40, 36)]

        closest_pair_result = closest_pair(input_points)

        assert closest_pair_result[0] == (33, 35)
        assert closest_pair_result[1] == (36, 34)
        assert closest_pair_result[2] == 3.1622776601683795

    def test_input_order_does_not_matter(self):
        input_points = [(2, 3), (3, 4), (5, 1), (12, 10), (12, 30), (40, 50)]
        shuffle(input_points)

        closest_pair_result = closest_pair(input_points)

        assert closest_pair_result[0] == (2, 3)
        assert closest_pair_result[1] == (3, 4)
        assert closest_pair_result[2] == 1.4142135623730951

    def test_input_of_length_one(self):
        input_points = [(2, 3)]

        closest_pair_result = closest_pair(input_points)

        assert closest_pair_result == None

    def test_input_of_length_two(self):
        input_points = [(2, 3), (3, 4)]

        closest_pair_result = closest_pair(input_points)

        assert closest_pair_result[0] == (2, 3)
        assert closest_pair_result[1] == (3, 4)
        assert closest_pair_result[2] == 1.4142135623730951

    def test_input_of_length_three(self):
        input_points = [(2, 3), (3, 4), (5, 6)]

        closest_pair_result = closest_pair(input_points)

        assert closest_pair_result[0] == (2, 3)
        assert closest_pair_result[1] == (3, 4)
        assert closest_pair_result[2] == 1.4142135623730951

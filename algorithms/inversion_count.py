from random import randint

def sort_and_count(input):
    if len(input) == 1:
        return input, 0

    arr_b, x = sort_and_count(input[:len(input)/2])
    arr_c, y = sort_and_count(input[len(input)/2:])
    arr_d, z = merge_and_count_split_inversions(arr_b, arr_c)

    return arr_d, (x + y + z)

def merge_and_count_split_inversions(left, right):
    output = []
    split_inversions = 0
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                output.append(left.pop(0))
            else:
                output.append(right.pop(0))
                split_inversions += len(left)
        elif left:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    return output, split_inversions

numbers = [1,5,3,4,2,6]
# numbers = [randint(0, 100) for x in range(100)]
print sort_and_count(numbers)

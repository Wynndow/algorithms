from random import randint

def inversion_count(input):
    if len(input) == 1:
        return input, 0
    arr_b, x = inversion_count(input[:len(input)//2])
    arr_c, y = inversion_count(input[len(input)//2:])
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

if __name__ == '__main__':
    numbers = [1,5,3,4,2,6]
    # numbers = [randint(0, 100) for x in range(100)]
    print(inversion_count(numbers))

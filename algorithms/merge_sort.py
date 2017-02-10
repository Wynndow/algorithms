from random import randint

def merge_sort(input):
    if len(input) <= 1:
        return input
    left = input[:len(input)//2]
    right = input[len(input)//2:]
    return _merge(merge_sort(left), merge_sort(right))

def _merge(left, right):
    output = []
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                output.append(left.pop(0))
            else:
                output.append(right.pop(0))
        elif left:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    return output

if __name__ == '__main__':
    numbers = [randint(0, 1000) for x in range(1000)]
    # numbers = [0.3, 0.5, 0.7, 0.1, 0.3, 0.2, 0.6, 0.1, 0.9]
    # print numbers
    print(merge_sort(numbers))

import sys

def sort_list(array):
    result = array.copy()
    max_value = -(sys.maxsize + 1)
    min_value = sys.maxsize
    for item in result:
        if item <= min_value:
            min_value = item
        if item >= max_value:
            max_value = item
    for i in range(0, len(result)):
        if result[i] == max_value:
            result[i] = min_value
        elif result[i] == min_value:
            result[i] = max_value
    if len(result): result.append(min_value)
    return result

print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))
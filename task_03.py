
def max_odd(array):
    result = None
    for item in array:
        if isinstance(item, int) or isinstance(item, float):
            if (result is None or item > result) and item % 2 != 0:
                result = int(item)
    return result

print(max_odd([1, 2, 3, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))
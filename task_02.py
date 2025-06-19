def coincidence(target_list=None, target_range=None):
    if target_range is None or target_list is None:
        return []
    result = []
    for item in target_list:
        if not item is None and (isinstance(item, int) or isinstance(item, float)):
            if target_range.start <= item < target_range.stop:
                result.append(item)
    return result

print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))

def multiply_numbers(inputs=None):
    if not inputs:
        return None
    result = None
    for element in str(inputs):
        if element.isdigit():
            if not result:
                result = int(element)
            else:
                result *= int(element)
    return result


print(multiply_numbers())
print(multiply_numbers('ss1'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(12.34))
print(multiply_numbers([5, 6, 4]))
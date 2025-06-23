
def multiply_numbers(inputs=None):
    if not inputs:
        return None
    result = None
    if isinstance(inputs, str):
        for element in inputs:
            if element.isdigit():
                if not result:
                    result = int(element)
                else:
                    result *= int(element)
    if isinstance(inputs, list):
        for element in inputs:
            if isinstance(element, int):
                if not result:
                    result = int(element)
                else:
                    result *= element
            if isinstance(element, str):
                if not result:
                    result = multiply_numbers(element)
                else:
                    result *= multiply_numbers(element)
    if isinstance(inputs, int):
        if inputs // 10 < 1:
            return inputs
        else:
            now = inputs
            while now % 10 > 1:
                if not result:
                    result = now % 10
                else:
                    result *= now % 10
                now //= 10
    if isinstance(inputs, float):
        both = str(inputs).split('.')
        first = int(both[0])
        second = int(both[1])
        return multiply_numbers(first) * multiply_numbers(second)
    return result


print(multiply_numbers())
print(multiply_numbers('ss1'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(12.34))
print(multiply_numbers([5, 6, 4]))
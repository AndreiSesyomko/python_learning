
def count_words(string):
    target = string.lower()
    result = {}
    current = ""
    for letter in target:
        if letter.isalpha():
            current += letter
        elif current != '':
            if current in result.keys():
                result[current] += 1
            else:
                result[current] = 1
            current = ""
    if current:
        if current in result.keys():
            result[current] += 1
        else:
            result[current] = 1
    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))


print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
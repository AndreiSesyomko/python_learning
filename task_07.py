def combine_anagrams(words_array):
    words = words_array.copy()
    words.sort()
    result = []
    checked = []
    for target in words:
        if target in checked:
            continue
        common = [target]
        isEquals = True
        for word in words:
            if word == target:
                continue
            count_equals = 0
            for letter in word:
                if len(target) != len(word):
                    continue
                if letter.lower() in target.lower():
                    if word.count(letter.lower()) != target.count(letter.lower()):
                        isEquals = False
                        break
                    count_equals += 1
            if count_equals == len(word) and isEquals and word not in common:
                common.append(word)
                checked.append(word)
        result.append(common)

    return result


print(combine_anagrams((["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])))
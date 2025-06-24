
def connect_dicts(dict1, dict2):
    first = dict1.copy()
    second = dict2.copy()
    temp1 = {}
    temp2 = {}
    result = {}
    sum1 = 0
    sum2 = 0
    for item in first:
        sum1 += first[item]
        if first[item] >= 10: temp1[f"{item}"] = first[item]
    for item in second:
        sum2 += second[item]
        if second[item] >= 10: temp2[f"{item}"] = second[item]
    if sum2 >= sum1:
        result = temp2.copy()
        for item in temp1:
            if not result.get(item):
                result[f"{item}"] = temp1[item]
    else:
        result = temp1.copy()
        for item in temp2:
            if not result.get(item):
                result[f"{item}"] = temp2[item]
    return dict(sorted(result.items(), key=lambda item: item[1]))

print(connect_dicts({  "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({  "a": 13, "b": 9, "d": 11 }, { "c": 12,  "a": 15 }))
print(connect_dicts({  "a": 14, "b": 12 }, { "c": 11,  "a": 15 }))
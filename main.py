
import string

def is_palindrome(target):
    target = target.replace(' ', '').lower()
    result = ""
    for i in range(0, len(target)):
        if target[i].isdigit() or target[i].isalpha():
            result += target[i]
    for i in range(0, int(len(result)/2)):
        if result[i] != result[-(i+1)]:
            return False
    return True

target = input("Enter a string: ")
print(is_palindrome(target))

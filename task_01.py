
def is_palindrome(target_string):
    target_string = str(target_string).replace(' ', '').lower()
    result = ""
    for i in range(0, len(target_string)):
        if target_string[i].isdigit() or target_string[i].isalpha():
            result += target_string[i]
    for i in range(0, int(len(result)/2)):
        if result[i] != result[-(i+1)]:
            return False
    return True

print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
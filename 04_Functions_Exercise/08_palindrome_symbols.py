def is_palindrome(some_number: str) -> bool:
    if some_number == some_number[::-1]:
        return True
    else:
        return False


list_of_integers = input().split(', ')
for number in list_of_integers:
    print(is_palindrome(number))

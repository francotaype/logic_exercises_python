def is_palindrome(s: str) -> bool:
    cleaned_string = ""
    for char in s:
        if char.isalnum():
            cleaned_string += char.lower()

    start = 0
    end = len(cleaned_string) - 1
    
    while start < end:
        if cleaned_string[start] != cleaned_string[end]:
            return False
        start += 1
        end -= 1

    return True

entrada = input("Enter a string: ")

if is_palindrome(entrada):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

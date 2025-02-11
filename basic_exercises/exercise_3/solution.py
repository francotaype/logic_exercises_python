def reverse_string(s: str) -> str:
    inverted_string = ""
    for i in range(len(s) - 1, -1, -1):  # Traverse the string from end to start
        inverted_string += s[i]
    return inverted_string

entrada = input("Enter a string of text: ")
print("Reversed string:", reverse_string(entrada))

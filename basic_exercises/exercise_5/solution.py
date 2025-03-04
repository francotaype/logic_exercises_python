def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

entrada = input("Enter a string: ")
vowels = count_vowels(entrada)

print(f"The number of vowels in the string is: {vowels}")

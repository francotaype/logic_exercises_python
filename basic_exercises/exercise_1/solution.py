def check_even_odd(number: int) -> str:
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("Please enter a number: "))
result = check_even_odd(number)
print(f"The number {number} is {result}.")

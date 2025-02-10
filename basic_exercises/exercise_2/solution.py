def find_largest(numbers: list) -> int:
    largest = numbers[0]
    
    for number in numbers:
        if number > largest:
            largest = number
            
    return largest

numbers = [10, 20, 35, 5, 99, 30]
largest_number = find_largest(numbers)
print(f"The largest number is: {largest_number}")
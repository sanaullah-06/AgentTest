def calculate_average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    average = total / len(numbers)  # Bug: Division by zero not handled
    return avrage  # Bug: Misspelled 'average' variable

numbers_list = [10, 20, 30, 40, 50]
result = calculate_avrage(numbers_list)  # Bug: Misspelled function name
print("The average is:", result)

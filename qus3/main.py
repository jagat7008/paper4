numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
numbers_dict = {'Even': even_numbers, 'Odd': odd_numbers}
print(numbers_dict)
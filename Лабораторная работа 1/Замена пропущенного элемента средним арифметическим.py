numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers[4] = 0
total = sum(numbers)
len_ = len(numbers)
average = round(total / len_, 2)
numbers[4] = average

print("Измененный список:", numbers)

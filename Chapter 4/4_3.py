for value in range(1, 6):
    print(value)


numbers = list(range(1, 15, 2))
print(numbers)

squares = []

for value in range(1,11):
#   square = value ** 2 теж саме якщо замінити значення нижче на змінну
    squares.append(value ** 2)

print(squares)


digits = []
for digit in range(1,1000000):
    digits.append(digit)
print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))
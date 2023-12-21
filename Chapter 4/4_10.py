squares = [number**2 for number in range(1, 10)]
print(squares)
# for number in squares:
#    print(number)


print(f"The first three item in the list are:\n{squares[:3]}")

print(f"Three items from the middle of the list are:\n{squares[3:6]}")

print(f"The last three items in the list are:\n{squares[-3:]}")

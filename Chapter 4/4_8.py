#squares = []
#
#for number in range(0, 11):
#    number = number**2
#    squares.append(number)
#    
#print(squares)



squares = [number**2 for number in range(0,11)]
print(squares)
for number in squares:
    print(number)
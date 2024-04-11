import math

while True:
    fnum = input("Input some numbet : ")
    snum = input("Input second number : ")
    if fnum or snum == "q":
        print("You just quit.")
        break
    """Калькулятор який ловить всяку дрянь замість цифр."""  
    try:
        
        kengoroo = sum([int(fnum), int(snum)])
        print(f"The sum is {kengoroo}.")
        
    except ValueError:
        print("Value error.")
        
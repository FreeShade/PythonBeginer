from name_function import get_formated_name

print("Enter 'q' at any time to quit.")
while True:
    first = input('\nPlease give me a first name: ')
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
        
    formated_name = get_formated_name(first, last)
    print(f"\tNeatly formatted name: {formated_name}.")
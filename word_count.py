def count_words(file_name):
    """Порахувати приблизну кількість слів у файлі."""
    try:
        with open(file_name, encoding='utf-8') as f:
            cont = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")        
    else:
        words = cont.split()
        num_words = len(words)
        print(f" The file {file_name} has about {num_words} words.")
        
file_names = ['/storage/emulated/0/Download/CodingPython/alice_in_wonderland.txt', '/storage/emulated/0/Download/CodingPython/pg2500.txt',
'/storage/emulated/0/Download/CodingPython/pg2701.txt', 'little_woman.txt']
for file_name in file_names:
    count_words(file_name)
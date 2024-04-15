

def c_words(file_name):
    """Порахувати приблизну кількість слів у файлі."""

    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except:
        pass
    else:
        words = contents.split()
        num_words_the = words.count("Alice")
        print(f"he file {file_name} has about {num_words_the} words")
file_name = r'/storage/emulated/0/Download/CodingPython/alice_in_wonderland.txt'
c_words(file_name)
        

#Відкриває читає все як треба
#відкрит файли dogs і cats і спіймати помилку пошуку  
fpath = r'/storage/emulated/0/Download/CodingPython/dogs.txt'

try:
    with open(fpath) as f:
        contents = f.read()
    print(contents)
except FileNotFoundError:
    print("Something go wrong, try 1 more time")
    

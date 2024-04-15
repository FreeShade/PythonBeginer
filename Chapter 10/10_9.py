#Відкриває читає все як треба
#відкрит файли dogs і cats і спіймати помилку пошуку  
# теж що і у попередній але тихо


fpath = r'/storage/emulated/0/Download/CodingPython/dogs.txt'

try:
    with open(fpath) as f:
        contents = f.read()
    print(contents)
except FileNotFoundError:
    pass
    

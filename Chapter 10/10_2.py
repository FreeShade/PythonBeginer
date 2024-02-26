# Зміни слово Python в файлі learning python  на якусь фігню.


path = r"Chapter 10\learning_python.txt"


with open(path) as text_object:
    lines = text_object.readlines()

learning_string = ""


for line in lines:
    learning_string += line.rstrip()

print(learning_string)
swap = learning_string.replace("python", "Ruby")
print(swap)

# зчитати файл learning_python кілька разів, по різному .
path = r"Chapter 10\learning_python.txt"

with open(path) as text_object:
    contents = text_object.read()
print(contents)

with open(path) as text_object:
    for line in text_object:
        print(line)

with open(path) as text_object:
    lines = text_object.readlines()

learning_string = ""
for line in lines:
    learning_string += line.rstrip()

print(learning_string)
print(len(learning_string))

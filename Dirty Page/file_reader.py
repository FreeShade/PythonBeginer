import os


os.chdir(r"C:\Users\Natrix\Desktop\repositories\PythonBeginer\Dirty Page")

print("Поточний каталог:", os.getcwd())


with open("pi_d.txt") as file_object:
    contents = file_object.read()
print(contents)

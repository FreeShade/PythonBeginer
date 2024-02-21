# import os


# os.chdir(r"C:\Users\Natrix\Desktop\repositories\PythonBeginer\Dirty Page")
# print("Поточний каталог:", os.getcwd())
# буква "r" в коді нижче допомагає не дублювати "\\" дуже зручно
file_path = r"C:\Users\Natrix\Desktop\repositories\PythonBeginer\Dirty Page\pi_d.txt"
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

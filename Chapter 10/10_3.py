# Гість , напиши програму що питиє ім'я та записує його у файл guest.txt

guest_name = input("Input your name please: ")

file_path = "Chapter 10\guest.txt"

with open(file_path, "a") as guest_file:
    guest_file.write(f"{guest_name.title()}")

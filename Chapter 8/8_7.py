# Напишіть функцію make_album(), що будує словник для опису музичного альбому.
# Вона приймає як аргумент ім'я музиканта та назву альбому,
# а повертає словник, що містить цю інформацію. Викличте функцію три рази для
# різних альбомів. Виведіть кожне повернення значення, щоб упевнитись -
# словники зберігають інформацію коректно.


def make_album(musician_name, album_name, song_score=None):
    """Повернути словник з інформацією про альбом."""
    album_info = {
        "Musician": musician_name,
        "Album": album_name,
    }
    if song_score:
        album_info["Song score"] = song_score
    return album_info


musicians_album = make_album("Jimi Hendrix", "Smoke on the water", 11)
print(musicians_album)

musicians_album = make_album("Jimi Hendrix", "Smoke on the water")
print(musicians_album)

musicians_album = make_album("Jimi", "Smoke", 11)
print(musicians_album)

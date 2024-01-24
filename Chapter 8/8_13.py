# Профіль користувача
# Скопіюйте код з user_profile.py (код знаходиться в Dirty Page)
# Створить свій профіль зі своїми параметрами

# Довільні ключові аргументи **kwargs


def build_profile(first, last, **user_info):
    """Створити словник, що міститиме всю інформацію про користувача."""
    user_info["first_name"] = first.title()
    user_info["last_name"] = last.title()
    return user_info


# user_profile = build_profile(
#     "albert", "einstein", location="princeton", field="physics"
# )

user_profile = build_profile(
    "alex", "liberty", location="Kyiv", field="millitary", mental="sad"
)

print(user_profile)

# **kwargs - набір неописаних ключових аргументів.

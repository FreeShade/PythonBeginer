those_who_vote = [
    "jen",
    "sarah",
    "edward",
    "phil",
    "alex",
    "abraham",
    "oleh",
    "mira",
    "lisa",
]

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    "alex": "python",
    "abraham": "rust",
    "oleh": "Java Script",
}

for name, language in favorite_languages.items():
    if name in those_who_vote:
        print(f"{name.title()} please chose you language.")
    else:
        print(f"{name.title(), }")

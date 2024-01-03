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

for name in those_who_vote:
    if name in favorite_languages.keys():
        print(f"{name.title()} thanks for your vote.")
    else:
        print(f"{name.title()} please chose you language.")

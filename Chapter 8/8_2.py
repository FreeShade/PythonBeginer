# Викличте функцію яка приймає 1 параметр, назву через .title()


def favorite_book(book):
    """It tell you a message about your favorite book"""
    print(f"One of my favorite book is {book.title()}.")


favorite_book(input("What is your favorite book? "))

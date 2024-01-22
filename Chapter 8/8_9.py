# Визначте список з коротких текстових повідомлень.
# Передайте його функції show_messages(), що виводитиме кожне з них.


def show_messages(messages_list):
    """Виводить кожне повідомлення зі списку"""
    for message in messages_list:
        print(message)


messages_list = ["This is a message.", "this is a message too.", "Same thing."]
show_messages(messages_list)

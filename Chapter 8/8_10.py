# Скрпіюйте код з вправи 8_9. Напишіть функцію send_message(), що виводить
# Кoжне текстове повідомлення та переміщує його до нового списку відправлених
# повідомлень sent_messages, вкінці виведіть обидва переліки.


def send_message(messages_list, sent_messages):
    """Вище прописав що воно робить , незграбно , але самостійно."""
    while messages_list:
        current_message = messages_list.pop()
        print(f"Printing message: {current_message}.")
        sent_messages.append(current_message)


def show_messages(some_messages_list):
    """Виводить кожне повідомлення зі списку"""
    for some_message in some_messages_list:
        print(some_message)


messages_list = ["This is a message.", "this is a message too.", "Same thing."]
sent_messages = []


send_message(messages_list, sent_messages)
show_messages(sent_messages)
show_messages(messages_list)

# вкінці виведіть обидва переліки.
print(messages_list)
print(sent_messages)

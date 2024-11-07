def send_mails(message, recipient, *, sender= input()):
    valid_ending = ('.ru', '.com', '.net')
    recipient = str(recipient)
    if '@' not in recipient or not recipient.endswith(valid_ending):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if '@' not in sender or not sender.endswith(valid_ending):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if sender == recipient:
        print('Нельзя отправить письмо самому себе! ')
    elif sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
message = input('Введите ваше сообщение: ')
recipient = input('Введите адрес получателя: ')
send_mails(message, recipient)
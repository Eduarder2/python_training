def correct_adress(adress):
    if not '@' in adress:
        return False
    elif not adress.endswith(('.com', '.ru', '.net')):
        return False
    else:
        return True

def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if not correct_adress(recipient) or not correct_adress(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на '
              f'адрес {recipient}.')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif 'university.help@gmail.com' == sender:
        print(f'Письмо успешно отправлено с адреса {sender} на '
              f'адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено '
              f'с адреса {sender} на адрес {recipient}.')
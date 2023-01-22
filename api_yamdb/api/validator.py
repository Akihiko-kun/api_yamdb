from django.contrib.auth.validators import UnicodeUsernameValidator


class UsernameRegValidator(UnicodeUsernameValidator):  # было лень писать в сериалезатаре и создал отдельный файл для
    # этого. тесты просили чтобы была валидация что нельзя больлше 150 и какие символы можно

    regex = r'^[\w.@+-]+\Z'
    flags = 0
    max_length = 150
    message = (f'Enter the correct username.'
               f'letters, digits and @/./+/-/_ only.'
               f'150 characters or fewer.')
    error_messages = {
        'invalid': f'150 characters or fewer.'
                   'letters, digits and @/./+/-/_ only.',
        'required': 'Поле не может быть пустым',
    }

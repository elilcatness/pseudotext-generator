def get_alphabet(langs: dict) -> str:
    while True:
        lang_code = input('Введите код языка: ').lower()
        alphabet = langs.get(lang_code, None)
        if alphabet is None:
            print(f'Язык с кодом {lang_code} не загружен!')
        elif not alphabet:
            print(f'Алфавит языка с кодом {lang_code} пуст!')
        else:
            return alphabet


def get_limit_mode(modes: list) -> str:
    modes_count = len(modes)
    while True:
        try:
            return modes[int(
                input('Выберите тип лимита: ' +
                      '\n'.join([f'{i + 1}. {modes[i]}'
                                 for i in range(modes_count)])
                      + '\n')) - 1][0]
        except (ValueError, IndexError):
            print(f'\nВведите число от 1 до {modes_count}\n')


def get_limit() -> int:
    while True:
        try:
            assert (limit := int(input('Введите лимит: '))) > 0
            return limit
        except (ValueError, AssertionError):
            print('Лимит должен быть представлен в виде натурального числа')

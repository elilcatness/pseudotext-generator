def get_alphabet(langs: dict):
    while True:
        lang_code = input('Введите код языка: ').lower()
        alphabet = langs.get(lang_code, None)
        if alphabet is None:
            print(f'Язык с кодом {lang_code} не загружен!')
        elif not alphabet:
            print(f'Алфавит языка с кодом {lang_code} пуст!')
        else:
            return alphabet

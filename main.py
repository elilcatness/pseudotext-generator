import os

from dotenv import load_dotenv

from src.constants import LIMIT_MODES, GEN_INIT_KEYS
from src.exceptions import GeneratorInitializationException
from src.gen import Generator
from src.interface import get_alphabet, get_limit, get_limit_mode
from src.utils import load_from_json, print_fail


def main():
    args = []
    for key in GEN_INIT_KEYS:
        var = os.getenv(key)
        if not var:
            return print_fail(f'Переменная {key} отсутствует или равна нулю в .env')
        try:
            assert (var := int(var)) > 0
        except (AssertionError, ValueError):
            return print_fail(f'Переменная {key} должна быть натуральным числом.\n'
                              f'Текущее значение: {var}')
        args.append(var)
    langs_filename = os.getenv('langs_filename', 'data/langs.json')
    if not (langs := load_from_json(langs_filename)):
        return print(f'Файл {langs_filename} пуст или не существует!')
    print(f'Загружено языков: {len(langs)}\n'
          f'Коды языков: {", ".join(langs.keys())}')
    alphabet = get_alphabet(langs)
    limit_mode = get_limit_mode(LIMIT_MODES)
    limit = get_limit()
    try:
        gen = Generator(alphabet, *args, limit_mode=limit_mode, limit=limit)
        with open('output.txt', 'w', encoding='utf-8') as f:
            text = gen.generate_text()
            print(text)
            # f.write(text)
    except GeneratorInitializationException as e:
        return print_fail(str(e))


if __name__ == '__main__':
    load_dotenv()
    main()

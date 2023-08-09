import json


def load_from_json(filename: str, convert_keys: bool = True):
    try:
        with open(filename, encoding='utf-8') as f:
            d = json.loads(f.read())
            if convert_keys:
                for key, val in d.items():
                    try:
                        converted_key = float(key)
                        d[converted_key] = d.pop(key)
                    except ValueError:
                        pass
            return d
    except FileNotFoundError:
        return None


def print_fail(text: str):
    print('\033[91m' + text + '\033[0m')


def main():
    print(load_from_json('../data/probs.json'))


if __name__ == '__main__':
    main()
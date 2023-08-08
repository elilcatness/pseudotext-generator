import json


def load_from_json(filename: str, convert_keys: bool = True):
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


def main():
    print(load_from_json('../data/probs.json'))


if __name__ == '__main__':
    main()
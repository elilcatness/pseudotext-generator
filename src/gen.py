import random

from src.exceptions import GeneratorInitializationException


class Generator:
    def __init__(self, alphabet: str, min_sentence_count: int, max_sentence_count: int,
                 min_words_per_sentence: int, max_words_per_sentence: int,
                 min_word_len: int, max_word_len: int,
                 limit_mode: str, limit: int, end_choices: dict = None):
        """
        :param alphabet:
        :param min_sentence_count:
        :param max_sentence_count:
        :param min_words_per_sentence:
        :param max_words_per_sentence:
        :param min_word_len:
        :param max_word_len:
        :param limit_mode:
        :param limit:
        :param end_choices:
        """

        self.alphabet = alphabet
        self.min_sentence_count = min_sentence_count
        self.max_sentence_count = max_sentence_count
        self.min_words_per_sentence = min_words_per_sentence
        self.max_words_per_sentence = max_words_per_sentence
        self.min_word_len = min_word_len
        self.max_word_len = max_word_len
        self.limit_mode = limit_mode
        self.limit = limit
        self.end_choices = end_choices if end_choices else dict()
        self.in_process = True

    def generate_word(self):
        if self.limit <= 0:
            self.in_process = False
            return ''
        word_length = random.randint(self.min_word_len, self.max_word_len)
        word = random.choice(self.alphabet)
        for i in range(word_length - 1):
            idx = self.alphabet.index(word[-1])
            s = random.choice(self.alphabet[:idx] + self.alphabet[idx + 1:])
            word += s
        return word

    def generate_sentence(self):
        sentence = ''
        words = []
        for i in range(self.max_words_per_sentence):
            is_last = i == self.max_words_per_sentence - 1
            word = self.generate_word()
            if len(word) < self.min_word_len:
                if not words:
                    return [], 0
                words[-1] += word
                break
            if 'symbols' in self.limit_mode:
                word_len = len(word)
                if self.limit_mode != 'symbols' or is_last:
                    word_len += 1
                self.limit -= word_len
            elif self.limit_mode == 'words':
                self.limit -= 1
        r = random.random()
        for p, s in sorted(self.end_choices.items(), key=lambda item: item[0]):
            if r < p:
                sentence += s
                break
        else:
            sentence += '.'
        return sentence.capitalize(), len(words)

    def generate_paragraph(self):
        sentences = []
        for _ in range(self.max_words_per_sentence):
            sentence, word_count = self.generate_sentence()
            if word_count < self.min_words_per_sentence:
                if sentences:
                    sentences[-1] = (
                            sentences[-1][:-1] +
                            sentence +
                            sentences[-1][-1])
                break
        return ' '.join(sentences)

    def generate_text(self):
        paragraphs = []
        while self.in_process:
            paragraphs.append(self.generate_paragraph())
        return '\n\n'.join(paragraphs)


def main():
    pass


if __name__ == "__main__":
    main()
    # paragraphs = random.randint(5, 20)
    # sentences_per_paragraph = random.randint(4, 7)
    # min_words_per_sentence = 3
    # max_words_per_sentence = 15
    #
    # pseudo_text = generate_text(paragraphs, sentences_per_paragraph, min_words_per_sentence, max_words_per_sentence)
    # print(pseudo_text)
    # with open('pseudo.txt', 'w', encoding='utf-8') as f:
    #     f.write(pseudo_text)

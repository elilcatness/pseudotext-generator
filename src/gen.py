import random

from src.constants import MIN_WORD_LEN, MAX_WORD_LEN
from src.exceptions import GeneratorInitializationException


class Generator:
    def __init__(self, alphabet: str, sentence_count: int,
                 words_per_sentence: int, min_word_len: int, max_word_len: int,
                 limit_mode: str, limit: int, end_choices: dict = None):
        """
        :param alphabet:
        :param sentence_count:
        :param words_per_sentence:
        :param min_word_len:
        :param max_word_len:
        :param limit_mode:
        :param limit:
        :param end_choices:
        """
        if limit_mode == 'words' and (
                real_limit := sentence_count * words_per_sentence) > limit:
            raise GeneratorInitializationException(
                f'При кол-ве предложений {sentence_count} '
                f'и кол-ве слов в них {words_per_sentence} '
                'объём текста должен быть задан не менее, '
                f'чем {real_limit} словами.\n'
                f'Текущий заданный лимит: {limit}')
        self.alphabet = alphabet
        self.sentence_count = sentence_count
        self.word_per_sentence = words_per_sentence
        self.min_word_len = min_word_len
        self.max_word_len = max_word_len
        self.limit_mode = limit_mode
        self.limit = limit
        self.end_choices = end_choices if end_choices else dict()
        self.in_process = True

    def generate_word(self):
        if self.limit <= 0:
            self.in_process = False
            return
        word_length = random.randint(MIN_WORD_LEN, MAX_WORD_LEN)
        word = random.choice(self.alphabet)
        for i in range(word_length - 1):
            idx = self.alphabet.index(word[-1])
            s = random.choice(self.alphabet[:idx] + self.alphabet[idx + 1:])
            word += s
        return word

    def generate_sentence(self):
        sentence = ''
        # punct_choices = {0.2: ",", 0.05: " -", 0.02: " -"}
        # prev_s = None
        # for i in range(word_count):
        #     word = generate_word()
        #     sentence += word
        #     if i < word_count - 1:
        #         r = random.random()
        #         for p, s in sorted(punct_choices.items(), key=lambda item: item[0]):
        #             if r < p and not (s in (":", " -") and prev_s == s):
        #                 sentence += s
        #                 prev_s = s
        #                 break
        #         sentence += " "
        # sentence = sentence[:-1]
        words = []
        for i in range(self.word_per_sentence):
            is_last = i == self.word_per_sentence - 1
            word = self.generate_word()
            if not word:
                break
            if 'symbols' in self.limit_mode:
                word_len = len(word)
                if self.limit_mode != 'symbols' or is_last:
                    word_len += 1
                self.limit -= word_len
            elif self.limit_mode == 'words':
                self.limit -= 1
        if not words:
            return
        r = random.random()
        for p, s in sorted(self.end_choices.items(), key=lambda item: item[0]):
            if r < p:
                sentence += s
                break
        else:
            sentence += '.'
        return sentence.capitalize()

    def generate_paragraph(self):
        sentences = []
        for _ in range(self.sentence_count):
            sentences.append(self.generate_sentence())
            if not self.in_process:
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

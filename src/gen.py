import os.path
import random
import string

from src.constants import MIN_WORD_LEN, MAX_WORD_LEN


def generate_word(alphabet: str, symbols_left: int):
    if symbols_left <= 0:
        return
    word_length = random.randint(MIN_WORD_LEN, MAX_WORD_LEN)
    word = random.choice(alphabet)
    for i in range(word_length - 1):
        idx = alphabet.index(word[-1])
        s = random.choice(alphabet[:idx] + alphabet[idx + 1:])
        word += s
    return word


def generate_sentence(word_count, alphabet: str, limit_mode: str,
                      limit: int, end_choices: dict = None):
    end_choices = end_choices if end_choices else dict()
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
    for i in range(word_count):
        is_last = i == word_count - 1
        if is_last:
            limit -= 1
        word = generate_word(alphabet, limit)
        if not word:
            break
        if 'symbols' in limit_mode:
            word_len = len(word)
            if limit_mode != 'symbols' and not is_last:
                word_len += 1
            limit -= word_len
        elif limit_mode == 'words':
            limit -= 1
    if not words:
        return
    r = random.random()
    for p, s in sorted(end_choices.items(), key=lambda item: item[0]):
        if r < p:
            sentence += s
            break
    else:
        sentence += '.'
    return sentence.capitalize()


def generate_paragraph(sentence_count: int, word_count: int, ):
    paragraph = ''

    for i in range(sentence_count):
        # word_count = random.randint(min_words, max_words)
        paragraph += generate_sentence(word_count)
        paragraph += ' '

    paragraph = paragraph.strip()
    return paragraph


def generate_text(paragraph_count, sentence_count, min_words, max_words):
    text = ""
    for i in range(paragraph_count):
        text += generate_paragraph(sentence_count, min_words, max_words)
        text += "\n\n"
    return text


def main():
    print(generate_word(string.ascii_lowercase, 100))


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

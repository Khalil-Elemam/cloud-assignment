from io import TextIOWrapper
from helper import english_stop_words
from re import split
from sys import exit



# Also you can use with statement here to read the file
def get_words(path: str) -> list[str]:
    file = None
    try:
        file: TextIOWrapper = open(path, "r")
        words: list[str] = []
        for line in file:
            words.extend([word for word in split(r"[^\w']+", line.lower())])
        return words
    except FileNotFoundError:
        print("File not found")
        exit(1)
    finally:
        if file:
            file.close()


def remove_stop_words(words: list[str]) -> list[str]:
    stop_words_set = english_stop_words
    return list(filter(lambda word: word not in stop_words_set and word != '', words))


def count_word(words: list[str]) -> dict[str, int]:
    counter: dict[str, int] = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter


if __name__ == "__main__":
    words: list[str] = remove_stop_words(get_words("paragraphs.txt"))
    counter = count_word(words)
    for unique_word in counter:
        print(f'{unique_word} ====>> {counter[unique_word]}')


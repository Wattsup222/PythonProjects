from word import Word


def create_word():
    word = Word()
    letters = word.individual_letters()
    for letter in letters:
        print(letter)


def main():
    create_word()


if __name__ == '__main__':
    main()

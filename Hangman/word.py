class Word:
    def __init__(self):
        self.letters = []
        self.word = "maple"

    def individual_letters(self):
        for letter in self.word:
            self.letters.append(letter)
        return self.letters
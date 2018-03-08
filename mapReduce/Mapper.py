class Mapper:
    def __init__(self, line):
        self.__line = line
        self.__wordsMap = []

    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, value):
        self.__line = value

    @property
    def wordsMap(self):
        return self.__wordsMap

    @wordsMap.setter
    def wordsMap(self, value):
        self.__wordsMap = value

    @staticmethod
    def symbolsFilter(w):
        w = w.split(",")[0]  # We create a list that contains all the divisions of the word created by the symbol "'" and we get the first one
        w = [letter for letter in w if not (letter in ';-?.,!:()')]  # we remove all the simbols, and create a word without symbols
        return ''.join(w).lower()  # we join all the elements from the list and transform every character to lowerCase

    def mapping(self, line_partial_part):
        for line in line_partial_part:
            words = line.split()
            for word in words:
                word_parsed = self.symbolsFilter(word)
                self.wordsMap.append((word_parsed, 1))

    @staticmethod
    def shuffle(listMapped):
        wordsDictionary = {}

        for line in listMapped:
            if wordsDictionary.has_key(line[0]):
                wordsDictionary[line[0]].append(line)
            else:
                wordsDictionary[line[0]] = []
                wordsDictionary[line[0]].append(line)

        return wordsDictionary







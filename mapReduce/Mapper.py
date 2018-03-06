import threading


class Mapper:
    def __init__(self):
        self.__line = ""
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
        w = [letter for letter in w if not (letter in ';-?.,!:')]  # we remove all the simbols, and create a word without symbols
        return ''.join(w).lower()  # we join all the elements from the list and transform every character to lowerCase

    def mapping(self):
        words = self.line.split()
        for word in words:
            word_parsed = self.symbolsFilter(word)
            self.wordsMap.append((word_parsed, 1))

    # wordsDictionary[w[0]].append(w)
    def shuffle(self):
        wordsDictionary = {}

        for mapItem in self.wordsMap:
            if wordsDictionary.has_key(mapItem[0]):
                wordsDictionary[mapItem[0]].append(mapItem)
            else:
                wordsDictionary[mapItem[0]] = []
                wordsDictionary[mapItem[0]].append(mapItem)

        return wordsDictionary

    """def shuffle_and_sort(self):
        tf = {}
        print "hola"
        L = self.line.split()
        print L
        for sublist in L:
            print sublist
            for p in sublist:
                # Append the tuple to the list in the map
                try:
                    tf[p[0]].append(p)
                except KeyError:
                    tf[p[0]] = [p]
        return tf"""

    def run(self):
        t = threading.Thread(target=self.mapping())
        t.start()


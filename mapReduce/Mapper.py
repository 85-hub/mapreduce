import threading
import Queue

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
        words = line_partial_part.split()
        for word in words:
            word_parsed = self.symbolsFilter(word)
            self.wordsMap.append((word_parsed, 1))


    # wordsDictionary[w[0]].append(w)
    def shuffle(self):
        wordsDictionary = {}
        #self.wordsMap = sorted(self.wordsMap, key=lambda tup: tup[0])
        #print "selfmap"
        #print self.wordsMap
        #utilizando diccionario
        for mapItem in self.wordsMap:
            if wordsDictionary.has_key(mapItem[0]):
                wordsDictionary[mapItem[0]].append(mapItem)
            else:
                wordsDictionary[mapItem[0]] = []
                wordsDictionary[mapItem[0]].append(mapItem)

        return wordsDictionary

    def run(self):
        for l in self.line:
            t = threading.Thread(target=self.mapping(l))
            t.start()




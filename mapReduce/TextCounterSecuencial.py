import sys

def getArgs():
    files = []

    for i in range(1, len(sys.argv)):
        files.append(sys.argv[i])

    return files

"""Aquesta funcio s'encarrega de treure simbols de les paraules d'un text, ja que nosaltres volem comptar les paraules sense simbols"""
def symbolsFilter(w):

    w = w.split(",")[0]  # We create a list that contains all the divisions of the word created by the symbol "'" and we get the first one
    w = [letter for letter in w if not (letter in ';-?.,!:()')]  # we remove all the simbols, and create a word without symbols
    return ''.join(w).lower()  # we join all the elements from the list and transform every character to lowerCase

def countWords(files):
    dict = {}  # We create the dictionary in which we will work
    for file in files:
        file = open(file)
        txt = file.read()
        txt = txt.split()
        file.close()
        for i in txt:  # we will be checking all the words, if it is the first time we'll add the word in the dictionary, otherwise, we will increase its value to 1
            i = symbolsFilter(i)
            if i in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
    return dict

def dirToTxt(dict):
    newFile = open("./resources/test_txt_files/resultSecuencial.txt","w")
    keyList = dict.keys()
    for w in keyList:
        newFile.write(w +" : " + str(dict[w]) + "\n")
    newFile.close()

if __name__  == '__main__':
    #TODO
    dict = {}
    dict = countWords(getArgs())
    dirToTxt(dict)
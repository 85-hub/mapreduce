import sys
from Mapper import *
from FileManager import *
from Reducer import *
import threading


def getArgs():
    files = []

    for i in range(1, len(sys.argv)):
        files.append(sys.argv[i])

    return files

def dirToTxt(dict):
    newFile = open("./resources/test_txt_files/resultMapReduce.txt","w")
    keyList = dict.keys()
    for w in keyList:
        newFile.write(w +" : " + str(dict[w]) + "\n")
    newFile.close()


def main():

    """Funcion principal, donde interactuamos con las 
       demas clases pasandoles los ficheros necesarios e 
       instanciando las clases del MapReduce"""

    num_cores = 4
    files = getArgs()

    file_manager = FileManager(files)
    lines_files = file_manager.split_in_lines()


    num_lines = len(lines_files)
    partialPart = num_lines/num_cores
    difference = num_lines - (partialPart * num_cores)

    mapper = Mapper("")
    for i in range(partialPart, (num_lines-partialPart) + 1, partialPart):
        t = threading.Thread(mapper.mapping(lines_files[i-partialPart:i]))
        t.start()

    t = threading.Thread(mapper.mapping(lines_files[num_lines - (partialPart+difference):num_lines]))
    t.start()

    shuffleDict = mapper.shuffle(mapper.wordsMap)

    reducer = Reducer()

    result = reducer.reduce(shuffleDict)

    dirToTxt(result)



if __name__ == "__main__":
    main()

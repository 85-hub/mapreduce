import sys
from Mapper import *
from FileManager import *
from Reducer import *


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

    files = getArgs()
    files_manager = FileManager(files)
    files_manager.run()
    #print "lista de lineas"
    #print files_manager.list_lines


    mapper = Mapper()
    mapMapped = []
    for text in files_manager.list_lines:
        for line_text in text:
            mapper.line = line_text
            mapper.run()
            #mapper.mapping()


    #print mapper.wordsMap

    shuffleDict = mapper.shuffle()

    #print shuffleDict

    reducer = Reducer()

    result = reducer.reduce(shuffleDict)

    dirToTxt(result)

if __name__ == "__main__":
    main()

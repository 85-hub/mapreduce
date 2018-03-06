import sys
from Mapper import *
from FileManager import *


def getArgs():
    files = []

    for i in range(1, len(sys.argv)):
        files.append(sys.argv[i])

    return files

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
    for text in files_manager.list_lines:
        for line_text in text:
            mapper.line = line_text
            mapper.mapping()
    print mapper.wordsMap
    print mapper.shuffle()


if __name__ == "__main__":
    main()

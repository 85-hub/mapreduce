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

    coreNumber = 4
    files = getArgs()
    files_manager = FileManager(files)
    files_manager.run()

    num_lines = len(files_manager.list_lines[0])+len(files_manager.list_lines[1])
    partialPart = num_lines/coreNumber

    files_manager.list_lines[0] = files_manager.list_lines[0]+files_manager.list_lines[1]

    list_splitted_lines = [l for l in open(files[0])] + [l for l in open(files[1])]

    mapper = Mapper("")
    for i in range(partialPart, num_lines+1, partialPart):
        mapper.line = list_splitted_lines[i-partialPart:i]
        mapper.run()
    #print files_manager.list_lines[0:partialPart]
    #[files_manager.list_lines[i:i + partialPart] for i in range(0, len(files_manager.list_lines), partialPart)]
    #print files_manager.list_lines

    #print files_manager.list_lines[1]

    """for text in files_manager.list_lines:
        #for line_text in text:
        #print line_text
        mapper = Mapper(line_text)

        #mapper.line = line_text
        mapper.run()
        #mapper.mapping()"""

    shuffleDict = mapper.shuffle()

    #print shuffleDict

    reducer = Reducer()

    result = reducer.reduce(shuffleDict)

    dirToTxt(result)

if __name__ == "__main__":
    main()

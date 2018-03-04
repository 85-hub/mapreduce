import sys
from FileManager import *

def main():

    """Funcion principal, donde interactuamos con las 
       demas clases pasandoles los ficheros necesarios e 
       instanciando las clases del MapReduce"""

    files = []

    for i in range(1, len(sys.argv)):
        files.append(sys.argv[i])

    files_manager = FileManager(files)
    files_manager.run()
    print files_manager.list_lines


if __name__ == "__main__":
    main()

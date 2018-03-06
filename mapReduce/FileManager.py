import threading

class FileManager:

    def __init__(self, file_text):
        self.__text_files = file_text
        self.__list_lines = []

    @property
    def text_files(self):
        return self.__text_files

    @text_files.setter
    def text_files(self, value):
        self.__text_files = value

    @property
    def list_lines(self):
        return self.__list_lines

    @list_lines.setter
    def list_lines(self, value):
        self.__list_lines = value

    """Funcion donde separaremos por lineas el txt, y lo 
       anadiremos a la lista de lineas del FileManager"""
    def split_in_lines(self, text):
        lines = text.splitlines()
        # print lines
        self.list_lines.append(lines)

    def run(self):
        strText = ""
        for i in range(0, len(self.text_files)):
            file_txt = open(self.text_files[i], "r")
            read_file = file_txt.read()
            strText += read_file

            #self.list_lines = strText
            self.split_in_lines(read_file)
        """threads = []
        for i in range(0, len(self.text_files)):
            #print "Archivo "+str(i)
            file_txt = open(self.text_files[i], "r")
            read_file = file_txt.read()
            t = threading.Thread(target=self.split_in_lines(read_file))

            t.start()
            threads.append(t)

        for t in threads:
            t.join()"""

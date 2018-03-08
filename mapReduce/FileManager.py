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
    def split_in_lines(self):
        lines_files = []
        for file in self.text_files:
            file_txt = open(file, "r")
            read_file = file_txt.read()
            lines_files += read_file.splitlines()
        return lines_files
class Room:
    __width: float
    __depth: float
    __height: float

    def __init__(self, width, depth):
        self.width = width
        self.depth = depth
        self.__height = 2.9

    @property
    def width(self):
        return self.__width

    @property
    def depth(self):
        return self.__depth

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        try:
            self.__width = float(width)
        except Exception:
            print('O valor informado da largura não é um número')
            exit()

    @depth.setter
    def depth(self, depth):
        try:
            self.__depth = float(depth)
        except Exception:
            print('O valor informado da profundiade não é um número')
            exit()

class Calculator:
    __wall_area: float
    __roof_area: float

    def calculate_wall_area(self, room):
        self.__wall_area: float = 2 * (room.width + room.depth) * room.height
        return self.__wall_area

    def calculate_roof_area(self, room):
        self.__roof_area: float = room.width * room.depth
        return self.__roof_area

    def calculate_required_liter(self):
        if self.__wall_area <= 0 or self.__roof_area <= 0:
            print(
                'Não é possível calcular a litragem com números negativos!'
            )
            exit()
        return (self.__wall_area + self.__roof_area) / 10

from dotenv import dotenv_values
config = dotenv_values(".env")


class Cell:
    def __init__(self, x, y, radius, mass, color):
        self.mass = mass
        self.position = (x, y)
        self.radius = radius
        self.__color = color

    def get_color(self):
        return self.__color


class WhiteCell(Cell):    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, int(config["CELL_WHITE_MASS"]), "white")


class RedCell(Cell):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, int(config["CELL_RED_MASS"]), "red")
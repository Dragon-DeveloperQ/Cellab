import numpy as np

from dotenv import dotenv_values
config = dotenv_values(".env")


class _Cell:
    def __init__(self, x, y, radius, mass, color):
        self.mass = mass
        self.position = (x, y)
        self.radius = radius
        self.__color = color

        dtype = [('id', 'i4'), ('value', '2i4')]
        self.__energy = np.array(dtype=dtype)

    def get_color(self):
        return self.__color
    
    def add_force(self, id, vector):
        self.__energy = np.append(self.__energy, (id, vector))
    
    def change_force(self, id, vector):
        self.__energy[np.where(self.__energy['id'] == id)[0]] = (id, vector)
    
    def remove_force(self, id):
        i = np.where(self.__energy['id'] == id)[0]
        if i.size > 0:
            self.__energy = np.delete(self.__energy, i)
        else:
            print('Не найдена сила, которую нужно удалить')


class WhiteCell(_Cell):    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, int(config["CELL_WHITE_MASS"]), "white")


class RedCell(_Cell):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, int(config["CELL_RED_MASS"]), "red")
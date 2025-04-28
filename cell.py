import numpy as np

from dotenv import dotenv_values
config = dotenv_values(".env")
GRAVITATION_CONST = float(config["GRAVITATION_CONST"])

class _Cell:
    def __init__(self, id, x, y, radius, mass, color):
        self.__id = id
        self.mass = mass
        self.position = (x, y)
        self.radius = radius
        self.__color = color
        self.__speed = (0, 0)

        dtype = [('id', 'i4'), ('value', '2f8')]
        self.__energy = np.array([0, (0, 0)], dtype=dtype)
    
    def get_id(self):
        return self.__id

    def get_color(self):
        return self.__color
    
    def add_force(self, id, vector):
        new_force = np.array([(id, vector)], dtype=self.__energy.dtype)
        self.__energy = np.append(self.__energy, new_force)
    
    def change_force(self, id, vector):
        self.__energy[np.where(self.__energy['id'] == id)[0]] = (id, vector)
        print(self.__energy[-1])
    
    def remove_force(self, id):
        i = np.where(self.__energy['id'] == id)[0]
        if i.size > 0:
            self.__energy = np.delete(self.__energy, i)
        else:
            print('Не найдена сила, которую нужно удалить')
    
    def move(self):
        for i in self.__energy['value']:
            self.__speed += i 
        self.position += self.__speed


class WhiteCell(_Cell):    
    def __init__(self, id, x, y, radius):
        super().__init__(id, x, y, radius, int(config["CELL_WHITE_MASS"]), "white")


class RedCell(_Cell):
    def __init__(self, id, x, y, radius):
        super().__init__(id, x, y, radius, int(config["CELL_RED_MASS"]), "red")


def create_force(a: _Cell, b: _Cell):
    # Сила с которой движется а по направлению к б
    rx = b.position[0] - a.position[0]
    ry = b.position[1] - a.position[1]
    return (GRAVITATION_CONST*b.mass/(rx**2), 
            GRAVITATION_CONST*b.mass/(ry**2))
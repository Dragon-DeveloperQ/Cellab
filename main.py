import pygame
import sys
import numpy as np
from random import randint
from dotenv import dotenv_values

import cell


# Загрузка конфига
config = dotenv_values(".env")
screen_width = int(config["SCREEN_WIDTH"])
screen_heigth = int(config["SCREEN_HEIGTH"])
fps = int(config["FPS"])


# Инициализация окна
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_heigth))
# Инициализация обьекта времени
clock = pygame.time.Clock()
# Запись начального времени выполненния программы
# start_program_time = pygame.time.get_ticks()


# Инициализация клеток
offsetX = screen_width // 2
offsetY = screen_heigth // 2

cells = np.empty(10, dtype=object)
for i in range(len(cells)):
    if i > 4:
        cells[i] = cell.WhiteCell(i, randint(0, screen_width), randint(0, screen_heigth), 5)
    else:
        cells[i] = cell.RedCell(i, randint(0, screen_width), randint(0, screen_heigth), 7)

#cell1 = cell.WhiteCell(-1, 0, 0, 10)
#cells = np.append(cells, cell1)





for i in cells:
    for j in cells: 
        vector = cell.create_force(i, j)
        j.add_force(i.get_id(), vector)  

        '''
        if i.get_color() == 'white':    
            for j in cells:
                if j.get_color() == 'red':
                    vector = cell.create_force(i, j)
                    j.add_force(i.get_id(), vector)  
        '''





# Инициализация цикла жизни
while True:
    screen.fill("black")


    # Обработка события выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Расчет данных для таймера
    # time = (pygame.time.get_ticks() - start_program_time) / 1000
    

    # Отрисовка пользовательской клетки (статичной)
    #x, y = pygame.mouse.get_pos()
    #cell1.position = (x, y)
    #pygame.draw.circle(screen, cell1.get_color(), (x, y), cell1.radius)

    
    for i in cells:  
        for j in cells:
            vector = cell.create_force(i, j)
            j.change_force(i.get_id(), vector)     
                    
    for i in cells:
        # Выполнить движение клетки с учетом всех сил
        i.move()
        # Отрисовать новое положениее клетки
        pygame.draw.circle(screen, i.get_color(), i.position, i.radius)
    

    # Обновление кадра
    pygame.display.flip()
    clock.tick(fps)
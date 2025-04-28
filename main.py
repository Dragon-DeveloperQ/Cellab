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
start_program_time = pygame.time.get_ticks()


# Инициализация клеток
offsetX = screen_width // 2
offsetY = screen_heigth // 2

cell1 = cell.WhiteCell(0, 0, 10)

cells = np.empty(10, dtype=object)
for i in range(len(cells)):
    if i <= 5:
        cells[i] = cell.WhiteCell(randint(0, screen_width), randint(0, screen_heigth), 5)
    else:
        cells[i] = cell.RedCell(randint(0, screen_width), randint(0, screen_heigth), 7)


# Инициализация цикла жизни
while True:
    screen.fill("black")

    # Обработка события выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Расчет данны для таймера
    time = (pygame.time.get_ticks() - start_program_time) / 1000
    

    x, y = pygame.mouse.get_pos()
    #pygame.draw.circle(screen, "white", (math.sin(time)*100 + offsetX, math.cos(time)*100 + offsetY), 10)
    pygame.draw.circle(screen, cell1.get_color(), (x, y), cell1.radius)
    for i in cells:
        pygame.draw.circle(screen, i.get_color(), i.position, i.radius)
    
    # Обновление кадра
    pygame.display.flip()
    clock.tick(fps)
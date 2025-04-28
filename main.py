import pygame
import sys
import math
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
cell3 = cell.WhiteCell(offsetX + 50, offsetY + 30, 10)
cell2 = cell.RedCell(offsetX, offsetY, 10)


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
    pygame.draw.circle(screen, cell3.get_color(), cell3.position, cell3.radius)
    pygame.draw.circle(screen, cell2.get_color(), cell2.position, cell2.radius)
    
    # Обновление кадра
    pygame.display.flip()
    clock.tick(fps)
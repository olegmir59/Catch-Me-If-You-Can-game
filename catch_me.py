import random
import pygame
import sys

# Инициализация pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра: Поймай меня, если сможешь")

# Загрузка изображения
icon = pygame.image.load("./img/icon.jpg")
icon = pygame.transform.scale(icon, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Масштабируем под размер экрана
#
target_img = pygame.image.load("img/бабочка2.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)


crow_img = pygame.image.load("img/Ворон2.jpg")  # {{ edit_1 }}
crow_img = pygame.transform.scale(crow_img, (400, 400))  # {{ edit_1 }}
crow_x = random.randint(0, SCREEN_WIDTH - 400)  # {{ edit_1 }}
crow_y = random.randint(0, SCREEN_HEIGHT - 400)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# Флаг для проверки, нажата ли мышь
start_game = False
catch_count = 0

# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_game = True  # Начинаем игру после нажатия мыши

    # Отрисовка
    if not start_game:
        screen.blit(icon, (0, 0))  # Отображаем изображение до начала игры
    else:
        # Здесь начинается логика вашей игры
        screen.fill((0, 0, 0))  # Например, просто чёрный экран
        # Добавьте свою игровую логику сюда

        screen.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка попадания по бабочке
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                crow_x = random.randint(0, SCREEN_WIDTH - 400)
                crow_y = random.randint(0, SCREEN_HEIGHT - 400)
                catch_count += 10
                print(catch_count)
            # Проверка попадания по ворону {{ edit_2 }}
            if crow_x < mouse_x < crow_x + 400 and crow_y < mouse_y < crow_y + 400:
                crow_x = random.randint(0, SCREEN_WIDTH - 400)
                crow_y = random.randint(0, SCREEN_HEIGHT - 400)
                catch_count -= 50
                print(catch_count)
        # Отрисовка ворона {{ edit_3 }}
        screen.blit(crow_img, (crow_x, crow_y))
        # Отрисовка бабочки
        screen.blit(target_img, (target_x, target_y))
        pygame.display.update()

    pygame.display.flip()

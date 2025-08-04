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

target3_img = pygame.image.load("img/бабочка3.jpg")
target3_img = pygame.transform.scale(target3_img, (80, 80))
target3_x = random.randint(0, SCREEN_WIDTH - 80)
target3_y = random.randint(0, SCREEN_HEIGHT - 80)


crow_img = pygame.image.load("img/Ворон2.jpg")  # {{ edit_1 }}
crow_img = pygame.transform.scale(crow_img, (400, 400))  # {{ edit_1 }}
crow_x = random.randint(0, SCREEN_WIDTH - 400)  # {{ edit_1 }}
crow_y = random.randint(0, SCREEN_HEIGHT - 400)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



# Флаг для проверки, нажата ли мышь
start_game = False
catch_count = 0
# Функция для проверки попадания мыши по объекту
def is_mouse_in_rect(mouse_pos, x, y, width, height):
    mx, my = mouse_pos
    return x < mx < x + width and y < my < y + height


def move_object_randomly(x, y, width, height, screen_width, screen_height):
    # Перемещаем объект в новое случайное место на экране
    new_x = random.randint(0, screen_width - width)
    new_y = random.randint(0, screen_height - height)
    return new_x, new_y


def move_all_objects():
    global target_x, target_y, target3_x, target3_y, crow_x, crow_y

    target_x, target_y = move_object_randomly(target_x, target_y, 80, 80, SCREEN_WIDTH, SCREEN_HEIGHT)
    target3_x, target3_y = move_object_randomly(target3_x, target3_y, 80, 80, SCREEN_WIDTH, SCREEN_HEIGHT)
    crow_x, crow_y = move_object_randomly(crow_x, crow_y, 400, 400, SCREEN_WIDTH, SCREEN_HEIGHT)


# Функция для обработки клика по объекту и его перемещения
def handle_click(mouse_pos, x, y, width, height, screen_width, screen_height):
    if is_mouse_in_rect(mouse_pos, x, y, width, height):
        # Перемещение объекта
        new_x = random.randint(0, screen_width - width)
        new_y = random.randint(0, screen_height - height)
        return True, new_x, new_y  # Успешный захват
    return False, x, y  # Нет захвата

# Основной цикл
while True:
    mouse_pressed = False
    mouse_pos = None

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
            mouse_pos = pygame.mouse.get_pos()
            if not start_game:
                start_game = True

    # Отрисовка
    if not start_game:
        screen.blit(icon, (0, 0))
    else:
        screen.fill(color)

        if mouse_pressed and mouse_pos:
            hit_any = False
            # Обработка клика по бабочке 2
            hit_butterfly_2, new_target_x, new_target_y = handle_click(
                mouse_pos, target_x, target_y, target_width, target_height,
                SCREEN_WIDTH, SCREEN_HEIGHT
            )
            if hit_butterfly_2:
                # target_x, target_y = new_target_x, new_target_y
                catch_count += 10
                hit_any = True
                print(catch_count)

            # Обработка клика по бабочке 3
            hit_butterfly_3, new_target3_x, new_target3_y = handle_click(
                mouse_pos, target3_x, target3_y, 80, 80,
                SCREEN_WIDTH, SCREEN_HEIGHT
            )
            if hit_butterfly_3:
                # target3_x, target3_y = new_target3_x, new_target3_y
                catch_count += 10
                hit_any = True
                print(catch_count)

            # Обработка клика по ворону
            hit_crow, new_crow_x, new_crow_y = handle_click(
                mouse_pos, crow_x, crow_y, 400, 400,
                SCREEN_WIDTH, SCREEN_HEIGHT
            )
            if hit_crow:
                # crow_x, crow_y = new_crow_x, new_crow_y
                catch_count -= 50
                hit_any = True
                print(catch_count)
            # все объекты меняют свои координаты
            if hit_any:
                move_all_objects()

        # Отрисовка объектов
        screen.blit(crow_img, (crow_x, crow_y))
        screen.blit(target_img, (target_x, target_y))
        screen.blit(target3_img, (target3_x, target3_y))

    # Отображение счёта
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Счёт: {catch_count}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()

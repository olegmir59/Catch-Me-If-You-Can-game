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


target4_img = pygame.image.load("img/бабочка4.jpg")
target4_img = pygame.transform.scale(target4_img, (120, 120))
target4_x = random.randint(0, SCREEN_WIDTH - 120)
target4_y = random.randint(0, SCREEN_HEIGHT - 120)


crow_img = pygame.image.load("img/Ворон2.jpg")  # {{ edit_1 }}
crow_img = pygame.transform.scale(crow_img, (400, 400))  # {{ edit_1 }}
crow_x = random.randint(0, SCREEN_WIDTH - 400)  # {{ edit_1 }}
crow_y = random.randint(0, SCREEN_HEIGHT - 400)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Новые переменные для отображения сообщения
show_crow_message = False
message_timer = 0
MESSAGE_DURATION = 1500  # 1.5 секунды

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
    global target_x, target_y, target3_x, target3_y, target4_x, target4_y, crow_x, crow_y

    target_x, target_y = move_object_randomly(target_x, target_y, 80, 80, SCREEN_WIDTH, SCREEN_HEIGHT)
    target3_x, target3_y = move_object_randomly(target3_x, target3_y, 80, 80, SCREEN_WIDTH, SCREEN_HEIGHT)
    target4_x, target4_y = move_object_randomly(target4_x, target4_y, 120, 120, SCREEN_WIDTH, SCREEN_HEIGHT)
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
    current_time = pygame.time.get_ticks()
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

        hit_any = False

        if mouse_pressed and mouse_pos:
            # Проверка попадания по бабочке 2
            if is_mouse_in_rect(mouse_pos, target_x, target_y, 80, 80):
                catch_count += 10
                hit_any = True

            # Проверка попадания по бабочке 3
            if is_mouse_in_rect(mouse_pos, target3_x, target3_y, 80, 80):
                catch_count += 10
                hit_any = True

            # Проверка попадания по бабочке 4
            if is_mouse_in_rect(mouse_pos, target4_x, target4_y, 120, 120):
                catch_count += 17
                hit_any = True

            # Проверка попадания по ворону
            if is_mouse_in_rect(mouse_pos, crow_x, crow_y, 400, 400):
                catch_count -= 50
                hit_any = True
                show_crow_message = True
                message_timer = current_time

            # Если был захват хотя бы одного объекта — перемещаем все
            if hit_any:
                move_all_objects()

        # Отрисовка объектов
        screen.blit(crow_img, (crow_x, crow_y))
        screen.blit(target_img, (target_x, target_y))
        screen.blit(target3_img, (target3_x, target3_y))
        screen.blit(target4_img, (target4_x, target4_y))


        # Отображение сообщения "КАР-КАР-КАР"
        if show_crow_message and current_time - message_timer < MESSAGE_DURATION:
            message_font = pygame.font.SysFont(None, 48)
            message_text = message_font.render("КАР-КАР-КАР", True, (255, 0, 0))  # Красный цвет
            text_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(message_text, text_rect)
        elif show_crow_message:
            show_crow_message = False  # Скрыть сообщение после истечения времени

    # Отображение счёта
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Счёт: {catch_count}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()

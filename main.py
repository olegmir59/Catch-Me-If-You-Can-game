import pygame

pygame.init()
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)

screen.blit(target_img, (target_x, target_y))
pygame.display.update()
pygame.quit()
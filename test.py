import pygame
pygame.init()
window_size=(800,600)
screen = pygame.display.set_mode(window_size)
cursor_img=pygame.image.load("F:\\College\\ТРПО\\TRPO Final\\Razvivushka\\images\\result_ezik_cursor.png")
pygame.mouse.set_visible(False)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    mouse_pos = pygame.mouse.get_pos()
    screen.fill((0,0,0))
    screen.blit(cursor_img,mouse_pos)
    pygame.display.update()
pygame.quit()
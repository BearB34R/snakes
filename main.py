import pygame

# Initialize pygame
pygame.init()

# Create the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

# game loop
run = True
while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True and player.left > 0:  # Check left boundary
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True and player.right < SCREEN_WIDTH:  # Check right boundary
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True and player.top > 0:  # Check top boundary
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True and player.bottom < SCREEN_HEIGHT:  # Check bottom boundary
        player.move_ip(0, 1)
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()

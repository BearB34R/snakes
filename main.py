import pygame
import time
import random

pygame.init()

# Define colors
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set display dimensions
dis_width = 800
dis_height = 600

# Set the size of each snake block
block_size = 20

# Set the speed of the snake
speed = 20

# Set fonts
font_style = pygame.font.SysFont(None, 50)


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    # Initial snake length
    snake_list = []
    length_of_snake = 1

    # Define initial position of food
    foodx = round(random.randrange(0, dis_width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, dis_height - block_size) / block_size) * block_size

    # Define initial score
    score = 0

    # Initialize Pygame window
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game')

    # Game loop
    while not game_over:
        while game_close:
            dis.fill(BLACK)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, RED)
            dis.blit(message, [dis_width / 6, dis_height / 3])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)
        pygame.draw.rect(dis, BLUE, [foodx, foody, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        for segment in snake_list:
            pygame.draw.rect(dis, GREEN, [segment[0], segment[1], block_size, block_size])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, dis_height - block_size) / block_size) * block_size
            length_of_snake += 1
            score += 10

        pygame.display.update()

        # Set game speed
        pygame.time.Clock().tick(speed)

    pygame.quit()
    quit()


gameLoop()

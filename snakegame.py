import pygame
#install the library if you don't have it with the command: pip install pygame
import random
import time

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Window dimensions
WIDTH = 600
HEIGHT = 400

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control game speed
clock = pygame.time.Clock()

# Snake settings
SNAKE_SIZE = 20
SNAKE_SPEED = 8

# Initialize font
font = pygame.font.SysFont(None, 48)

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(window, GREEN, [x, y, SNAKE_SIZE, SNAKE_SIZE])

def message(msg, color):
    text = font.render(msg, True, color)
    window.blit(text, [WIDTH/6, HEIGHT/3])

def game_loop():
    game_over = False
    game_close = False

    # Initial snake position and movement
    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE
    food_y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE

    while not game_over:
        while game_close:
            window.fill(BLACK)
            message("Game Over! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            # Handle game over input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -SNAKE_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = SNAKE_SIZE
                    x_change = 0

        # Update snake position
        x += x_change
        y += y_change

        # Check boundaries collision
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        window.fill(BLACK)
        pygame.draw.rect(window, RED, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check self collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        pygame.display.update()

        # Check food collision
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE
            food_y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Start the game
game_loop()

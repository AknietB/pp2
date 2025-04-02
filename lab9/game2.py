import pygame
import time
import random

# Game speed and screen size
speed = 10
height = 700
width = 700

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
fps = pygame.time.Clock()

# Snake initial position and body structure
snake_position = [100, 50]
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# Generate fruit with random position and weight
fruit_position = [random.randrange(1, (width // 10)) * 10,
                  random.randrange(1, (height // 10)) * 10]
fruit_weight = random.choice([10, 20, 30])  # Random food value
fruit_spawn = True
fruit_timer = time.time()  # Track fruit lifespan
fruit_lifetime = 5  # Time before food disappears

direction = 'RIGHT'
change_to = direction

# Score and Level
score = 0
level = 1
last_score_checkpoint = 0  # Used to track level increments

def show_score(choice, color, font, size):
    """ Display the score and level on the screen """
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score: {score}', True, color)
    level_surface = score_font.render(f'Level: {level}', True, color)
    score_rect = score_surface.get_rect()
    level_rect = level_surface.get_rect(topright=(width - 10, 10))
    screen.blit(score_surface, score_rect)
    screen.blit(level_surface, level_rect)

def game_over():
    """ Display the game over screen and exit """
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(f'Your score is: {score}', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:
    # Event handling for user input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Prevent the snake from reversing
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake movement mechanics
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += fruit_weight  # Add weight value to score
        fruit_spawn = False
    else:
        snake_body.pop()

    # Generate a new fruit if eaten or expired
    if not fruit_spawn or time.time() - fruit_timer > fruit_lifetime:
        fruit_position = [random.randrange(1, (width // 10)) * 10,
                          random.randrange(1, (height // 10)) * 10]
        fruit_weight = random.choice([10, 20, 30])  # Assign new random weight
        fruit_spawn = True
        fruit_timer = time.time()  # Reset timer

    # Update screen
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Collision detection with walls
    if snake_position[0] < 0 or snake_position[0] > width - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > height - 10:
        game_over()
    
    # Collision detection with itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Display score and level
    show_score(1, white, 'times new roman', 35)
    pygame.display.update()

    # Increase speed and level when reaching a score milestone
    if score % 30 == 0 and score != last_score_checkpoint:
        speed += 1
        level += 1
        last_score_checkpoint = score

    fps.tick(speed)

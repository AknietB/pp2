import pygame
import time
import random
import psycopg2

conn = psycopg2.connect(database="ernar", user="postgres", password="akniet07", host="localhost", port="5432")
cur = conn.cursor()

def create_tables():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS "User" (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL
    );
    CREATE TABLE IF NOT EXISTS user_score (
        score_id SERIAL PRIMARY KEY,
        user_id INT REFERENCES "User"(user_id),
        level INT NOT NULL,
        score INT NOT NULL
    );
    """)
    conn.commit()

def get_user_id(username):
    cur.execute("SELECT user_id FROM \"User\" WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        cur.execute("INSERT INTO \"User\" (username) VALUES (%s) RETURNING user_id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id

def insert_user_score(user_id, level, score):
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    conn.commit()


speed = 10
height = 700
width = 700
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((width, height))
fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruit_position = [random.randrange(1, (width // 10)) * 10,
                  random.randrange(1, (height // 10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0
level = 1
last_score_checkpoint = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    level_surface = score_font.render('Level: ' + str(level), True, color)
    score_rect = score_surface.get_rect()
    level_rect = level_surface.get_rect(topright=(width - 10, 10))
    screen.blit(score_surface, score_rect)
    screen.blit(level_surface, level_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your score is: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # Сохраняем результат в базу
    insert_user_score(user_id, level, score)

    time.sleep(2)
    pygame.quit()
    conn.close()
    quit()

create_tables()
username = input("Enter your username: ")
user_id = get_user_id(username)


cur.execute("""
SELECT level FROM user_score 
INNER JOIN "User" ON user_score.user_id = "User".user_id 
WHERE "User".username = %s ORDER BY score_id DESC LIMIT 1
""", (username,))
row = cur.fetchone()
if row:
    print(f"Welcome back, {username}! Your current level is: {row[0]}")
else:
    print(f"Welcome, {username}! New player.")

def pause_game():
    print("Game paused")  
    font = pygame.font.SysFont("bahnschrift", 35)
    pause_surface = font.render("Game Paused. Press 'P' to Resume or 'S' to Save", True, white)
    pause_rect = pause_surface.get_rect(center=(width / 2, height / 2))
    screen.blit(pause_surface, pause_rect)
    pygame.display.update()

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False 
                    print("Resuming game...") 
                elif event.key == pygame.K_s:

                    insert_user_score(user_id, level, score)
                    print("Game saved successfully!") 
                    paused = False


while True:
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
            if event.key == pygame.K_p:
                pause_game() 

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (width // 10)) * 10,
                          random.randrange(1, (height // 10)) * 10]
    fruit_spawn = True

    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > width - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > height - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, 'times new roman', 35)
    pygame.display.update()

    if score % 30 == 0 and score != last_score_checkpoint:
        speed += 1
        level += 1
        last_score_checkpoint = score

    fps.tick(speed)
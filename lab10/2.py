import pygame
import random
import sys
import psycopg2
import time

# Initialize Pygame
pygame.init()

# Database connection
conn = psycopg2.connect(database="ernar", user="postgres", password="akniet07", host="localhost", port="5432")
cur = conn.cursor()

# Define User and User_Score tables
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

# Game setup
display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)

# Helper functions
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width / 6, display_height / 3])

def show_score(score, level):
    value = score_font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    dis.blit(value, [0, 0])

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

def show_current_level(username):
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

# Snake and Food classes
class Snake:
    def _init_(self):
        self.length = 1
        self.positions = [[display_width // 2, display_height // 2]]
        self.direction = [0, 0]

    def move(self):
        head = list(self.positions[-1])
        head[0] += self.direction[0]
        head[1] += self.direction[1]
        self.positions.append(head)
        if len(self.positions) > self.length:
            del self.positions[0]

    def grow(self):
        self.length += 1

    def draw(self, dis):
        for pos in self.positions:
            pygame.draw.rect(dis, (0, 255, 0), [pos[0], pos[1], snake_block, snake_block])

    def check_collision(self):
        head = self.positions[-1]
        return (
            head[0] >= display_width or head[0] < 0 or
            head[1] >= display_height or head[1] < 0 or
            head in self.positions[:-1]
        )

class Food:
    def _init_(self):
        self.x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    def draw(self, dis):
        pygame.draw.rect(dis, (255, 0, 0), [self.x, self.y, snake_block, snake_block])

    def relocate(self):
        self.x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

# Game logic
def game_loop(username):
    user_id = get_user_id(username)
    snake = Snake()
    food = Food()
    game_over = False
    game_close = False
    level = 1
    score = 0
    snake_speed = 15

    while not game_over:
        while game_close:
            dis.fill((50, 153, 213))
            message("You lost! Press Q-Quit or C-Play Again", (213, 50, 80))
            show_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop(username)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.direction = [-snake_block, 0]
                elif event.key == pygame.K_RIGHT:
                    snake.direction = [snake_block, 0]
                elif event.key == pygame.K_UP:
                    snake.direction = [0, -snake_block]
                elif event.key == pygame.K_DOWN:
                    snake.direction = [0, snake_block]

        snake.move()

        if snake.check_collision():
            insert_user_score(user_id, level, score)
            game_close = True

        dis.fill((0, 0, 0))
        food.draw(dis)
        snake.draw(dis)
        show_score(score, level)
        pygame.display.update()

        if snake.positions[-1][0] == food.x and snake.positions[-1][1] == food.y:
            food.relocate()
            snake.grow()
            score += 10
            if score % 50 == 0:
                level += 1
                snake_speed += 2

        clock.tick(snake_speed)

def main():
    create_tables()
    username = input("Enter your username: ")
    show_current_level(username)
    game_loop(username)
    conn.close()
    print("Database connection closed.")

if __name__ == "_main_":
    main()
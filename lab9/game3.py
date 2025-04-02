import pygame

# Initialize pygame
pygame.init()

# Set up frame rate
fps = 60
framepersec = pygame.time.Clock()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Default settings
active_figure = 0
white = (255, 255, 255)
active_color = white
painting = []

def draw_menu(color):
    pygame.draw.rect(screen, 'grey', [0, 0, width, 70])  # Menu background
    pygame.draw.line(screen, 'black', (0, 70), (width, 70), 3)  # Border line
    
    # Brush options
    circle_brush = [pygame.draw.rect(screen, 'black', [0, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'white', (25, 35), 15)
    
    rect_brush = [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]
    pygame.draw.rect(screen, 'white', [76.5, 16, 37, 30], 2)
    
    square_brush = [pygame.draw.rect(screen, 'black', [140, 10, 50, 50]), 2]
    pygame.draw.rect(screen, 'white', [146.5, 16, 30, 30], 2)

    right_triangle_brush = [pygame.draw.rect(screen, 'black', [210, 10, 50, 50]), 3]
    pygame.draw.polygon(screen, 'white', [(235, 20), (215, 50), (255, 50)], 2)

    equilateral_triangle_brush = [pygame.draw.rect(screen, 'black', [280, 10, 50, 50]), 4]
    pygame.draw.polygon(screen, 'white', [(305, 15), (285, 50), (325, 50)], 2)

    rhombus_brush = [pygame.draw.rect(screen, 'black', [350, 10, 50, 50]), 5]
    pygame.draw.polygon(screen, 'white', [(375, 15), (360, 35), (375, 55), (390, 35)], 2)
    
    eraser=pygame.image.load('Labs\lab8\eraser (1).png')
    eraser_rect=eraser.get_rect(topleft=(width-150,7))
    eraser_rect.width=eraser_rect.height=25
    screen.blit(eraser,[width-150,7,25,25])
    
    brush_list = [circle_brush, rect_brush, square_brush, right_triangle_brush, equilateral_triangle_brush, rhombus_brush]
    
    # Active color display
    pygame.draw.circle(screen, color, (500, 35), 30)
    pygame.draw.circle(screen, 'dark grey', (500, 35), 30, 3)

    # Color options
    colors = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]
    color_rects = [pygame.draw.rect(screen, colors[i], [width - (i % 4) * 30 - 35, (i // 4) * 30 + 10, 25, 25]) for i in range(len(colors))]
    color_rects.append(eraser_rect)
    colors.append((255, 255, 255))  # White color for eraser

    return brush_list, color_rects, colors

def draw_painting(paints):
    for color, pos, figure in paints:
        if figure == 0:
            pygame.draw.circle(screen, color, pos, 20, 2)
        elif figure == 1:
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20], 2)
        elif figure == 2:
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 30, 30], 2)
        elif figure == 3:
            pygame.draw.polygon(screen, color, [(pos[0], pos[1] - 20), (pos[0] - 20, pos[1] + 20), (pos[0] + 20, pos[1] + 20)], 2)
        elif figure == 4:
            pygame.draw.polygon(screen, color, [(pos[0], pos[1] - 20), (pos[0] - 20, pos[1] + 15), (pos[0] + 20, pos[1] + 15)], 2)
        elif figure == 5:
            pygame.draw.polygon(screen, color, [(pos[0], pos[1] - 20), (pos[0] - 15, pos[1]), (pos[0], pos[1] + 20), (pos[0] + 15, pos[1])], 2)

run = True
while run:
    framepersec.tick(fps)
    screen.fill("white")
    
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    
    brushes, colors, rgbs = draw_menu(active_color)
    
    if left_click and mouse[1] > 85:
        painting.append((active_color, mouse, active_figure))
    draw_painting(painting)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]
            for i in brushes:
                if i[0].collidepoint(event.pos):
                    active_figure = i[1]
    
    pygame.display.flip()

pygame.quit()

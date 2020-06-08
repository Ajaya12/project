import pygame
import time
import random

WIDTH = 450
HEIGHT = 500
FPS = 30

WHITE = (255, 255, 255)
BLUE = (0, 0, 0)
GREEN = (0, 255, 0)
COLOR = (0, 255, 255)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Recursive Backtracker')
icon = pygame.image.load('bg.png')
clock = pygame.time.Clock()

x = 0
y = 0
w = 20
grid = []
visited = []
stack = []
solution = {}

def grid_construct(x ,y ,w):
    for i in range(1, 21):
        x = 20
        y = y + 20
        for j in range(1, 21):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           # top of cell
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   # right of cell
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   # bottom of cell
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])
            grid.append((x, y))
            x = x + 20

def visit_up(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y - w + 1,19 , 39), 0)     #to fill
    pygame.display.update()

def visit_down(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1,19 , 39), 0)
    pygame.display.update()

def visit_right(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1,39 , 19), 0)
    pygame.display.update()

def visit_left(x, y):
    pygame.draw.rect(screen, BLUE, (x - w + 1, y + 1,39 ,19), 0)
    pygame.display.update()

def single_cell(x, y):
    pygame.draw.rect(screen, GREEN, (x + 1, y + 1,18 ,18), 0)
    pygame.display.update()

def back_tracking(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1,18 ,18), 0)
    pygame.display.update()

def solution_cell(x, y):
    pygame.draw.rect(screen, COLOR, (x + 8, y + 8,5 ,5), 0)
    pygame.display.update()

def draw_maze(x, y):
    single_cell(x, y)
    stack.append((x, y))
    visited.append((x, y))
    while len(stack) > 0:
        time.sleep(.05)
        cell = []
        if (x + w, y) not in visited and (x + w, y) in grid:
            cell.append("right")                                 

        if (x - w, y) not in visited and (x - w, y) in grid:      
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in grid:     
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in grid:     
            cell.append("up")

        if len(cell) > 0:
            cell_chosen = (random.choice(cell))
            
            if cell_chosen == "right":
                visit_right(x, y)
                solution[(x + w, y)] = x, y                       
                x = x + w                                         
                visited.append((x, y))                            
                stack.append((x, y))
            
            elif cell_chosen == "left":
                visit_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                visit_down(x, y)
                solution[(x , y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                visit_up(x, y)
                solution[(x , y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                                  
            single_cell(x, y)                                     
            time.sleep(.05)                                       
            back_tracking(x, y)

def plot_route_back(x,y):
    solution_cell(x, y)
    while (x, y) != (20,20):
        x, y = solution[x, y]
        solution_cell(x, y)
        time.sleep(.1)

screen.blit(icon , (0, 0))
x, y = 20, 20
grid_construct(40, 0, 20)
draw_maze(x, y)
plot_route_back(400, 400)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


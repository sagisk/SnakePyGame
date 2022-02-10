import pygame
import sys
from Draw import Draw
from Snake import Snake
from Food import Food
from Graph import Graph
from Model import Model

screen_width = 480
screen_height = 480
gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize

def main(screen_width, screen_height, gridsize):
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    d = Draw(surface)
    d.drawGrid(grid_height, grid_width, gridsize)

    snake_color = (17, 24, 47)
    food_color = (223, 163, 49)
    position = [((screen_width / 2), (screen_height / 2))]

    snake = Snake(position)
    food = Food()
    
    myfont = pygame.font.SysFont("monospace", 16)


    g = Graph()
    g.grid_to_graph()
    path = [(240, 240), (240, 220),(240,200)]#g.DFS(s = position[0], t = (240,200))
    model = Model('model_name')
    while(True):
        clock.tick(10) #fps
        snake.handle_keys()
        d.drawGrid(grid_height, grid_width, gridsize)
        x = food.position
        f_x, f_y = x[0]
        snake.move()
        x,y = snake.get_head_position()
        head = snake.get_head_position()
        if x == f_x and y == f_y:
            snake.length += 1
            snake.score += 1
            food.set_food_position(grid_height, grid_width, gridsize)
            g = Graph()
            g.grid_to_graph()
        d.draw(snake.position, snake_color)
        d.draw(food.position, food_color)
        screen.blit(surface, (0, 0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5, 10))
        pygame.display.update()

main(480, 480, 20)
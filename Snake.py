import numpy as np
import pygame
import random
import sys

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

# change this.
screen_width = 480
screen_height = 480
gridsize = 20

class Snake:
    def __init__(self, position):
        self.length = 0
        self.score = 0
        self.position = position
        self.direction = random.choice([up, left, right, down])#[up, left, right, down]
        self.pos = [(0, 0), (20, 0), (40, 0), (40, 20), (20, 20), (0, 20), (0, 40)]

    def get_head_position(self):
        return self.position[0]
    
    def get_position(self):
        return self.position

    def get_state(self):
        head = self.get_head_position()
        positions = self.get_position()
        left_action, right_action, up_action = [1]*3 
        if (head[0] - gridsize, head[1]) in positions:
            left_action = 0
        else:
            left_action = 1
        if (head[0] + gridsize, head[1]) in positions:
            right_action = 0
        else:
            righ_action = 1
        if (head[0], head[1] - gridsize) in positions:
            up_action = 0
        else:
            up_action = 1
        return [self.direction, left_action, right_action, up_action]
    
    def is_suicide(self):
        x, y = self.get_head_position()
        border_x = screen_height - gridsize
        border_y = screen_width - gridsize
        if x > border_x or y > border_y:
            print(x,y)
            return True
        # collide
        position = self.get_position()
        #print(position)
        head_position = self.get_head_position()
        if head_position in position[2:]:
            if all([pos_x[0] == x for pos_x in position]):
                return False
            elif all([pos_y[1] == y for pos_y in position]):
                return False
            return True
        return False

    def possible_action(self, pos):
        positions = self.get_position()
        return pos in positions[0:]

    def move_by_path(self, path):
        curr_pos = self.get_head_position()
        try:
            new_pos = path[0]
            
            if self.is_suicide():
                self.reset()
            self.position.insert(0, new_pos)
            path.pop(0)
            #print("Pop", path)
            if len(self.position) > self.length + 1:
                self.position.pop()
        except IndexError:
            print('Eat')

    def move(self, rand = False):
        curr_pos = self.get_head_position()
        if rand:
            x, y = random.choice([up, left, right, down])
        else:
            x, y = self.direction
        new_pos = (int((curr_pos[0] + (x*gridsize)) % screen_width), int((curr_pos[1] + (y*gridsize)) % screen_height))
        if self.is_suicide():
            self.reset()
        self.position.insert(0, new_pos)
        if len(self.position) > self.length + 1:
            self.position.pop()
    
    def turn(self, direction):
        #if self._is_colide(direction): return
        self.direction = direction

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)

    def reset(self):
        print('RESET')
        self.length = 0
        self.score = 0
        self.position = [((screen_width / 2), (screen_height / 2))]
        #self.direction = random.choice([up, left, right, down])
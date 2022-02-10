import random

class Food:
    def __init__(self, image = None):
        self.position = [(240, 200)]
        self.image = image
    
    def set_food_position(self, grid_height, grid_width, gridsize):
        self.position[0] = (random.randint(0, grid_width - 1)*gridsize,
                            random.randint(0, grid_height - 1)*gridsize)
    
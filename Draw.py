import pygame

gridsize = 20

class Draw:
    def __init__(self, surface):
        self.surface = surface


    def draw(self, positions, color):
        for p in positions:
            rectangle = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(self.surface, color, rectangle)
            pygame.draw.rect(self.surface, (93, 216, 228), rectangle, 1)


    def drawGrid(self, grid_height, grid_width, gridsize):
        for y in range(0, int(grid_height)):
            for x in range(0, int(grid_width)):
                rectangle = pygame.Rect((x*gridsize,y*gridsize), (gridsize, gridsize))
                pygame.draw.rect(self.surface, (93, 216, 228), rectangle)
    
 
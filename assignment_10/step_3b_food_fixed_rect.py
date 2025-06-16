# Stockdale Assignment 10 - Step 3B: Food Object Using Fixed Position with Vector2 and Rect
#
# Notes from: https://opal.ils.unc.edu/~lblakej/snake-game/03-add-food/#drawing-the-food-object
#
# The pygame Vector2 class is a data structure that holds x and y attributes,
# similar to the position coordinates needed for game objects.
#
# The Vector2 class provides useful methods for manipulating 2D vectors,
# making it easier to handle positions and movements in the game.
#
# The Food object uses a Vector2 variable to store its position in terms of grid cells,
# not pixels. For example:
#
# self.position = Vector2(5, 6)
#
# This means the food is located at the 6th column (x=5) and 7th row (y=6) of the grid,
# with counting starting at 0.
#
# To use Vector2, it must be imported from pygame.math:
# from pygame.math import Vector2
#
# When drawing the food, Pygame uses three main concepts:
# - The display surface created by pygame.display.set_mode(), which is the canvas shown on screen.
# - Regular surfaces that can be drawn on and later blitted onto the display surface.
# - Rects (pygame.Rect), rectangular areas defined by position and size, used for drawing and collision detection.
#
# Rects simplify manipulation and drawing of objects.
#
# This step creates a Food class that has a fixed position on the grid
# and draws itself as a rectangle on the screen.

import pygame, sys
from pygame.math import Vector2

pygame.init()

cell_size = 30
number_of_cells = 25

SCREEN_WIDTH = cell_size * number_of_cells
SCREEN_HEIGHT = cell_size * number_of_cells

FPS = 60

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Snake Game")

clock = pygame.time.Clock()

class Food:
    def __init__(self):
        # Position of food in grid cells (x=5, y=6)
        self.position = Vector2(5, 6)
        self.size = cell_size
        # Create a Rect for drawing and collision using position and size
        self.rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, self.size, self.size)

    def draw(self, surface):
        # Draw the food as a red rectangle on the given surface
        pygame.draw.rect(surface, RED, self.rect)

def main():
    food = Food()

    while True:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(GREEN)

        # Draw the food
        food.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

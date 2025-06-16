# Stockdale Assignment 10 - Step 3C: Food Object with Fixed Position and Image
#
# Notes from: https://opal.ils.unc.edu/~lblakej/snake-game/03-add-food/#drawing-the-food-object
#
# The Food object needs a rect to contain it.
# The rect is invisible but helps position and draw the food on the screen.
#
# The rect requires four values: x and y coordinates of the top-left corner,
# and the width and height of the rectangle.
#
# Since the game uses a grid, multiply the x and y cell positions by the cell size:
#
# x = self.position.x * cell_size
# y = self.position.y * cell_size
#
# The width and height will be equal to cell_size.
#
# In the last step the food was drawn as a colored square using pygame.draw.rect(surface, color, rect).
# In this step, instead of drawing a square, an image will be loaded and drawn.
#
# To load an image, use pygame.image.load() with the file path to the image:
# food_surface = pygame.image.load("graphics/food.png")
#
# The blit() method draws one surface onto another.
# Use screen.blit(food_surface, food_rect) to draw the food image on the screen at the position defined by food_rect.
#
# This method requires the display surface, the image surface, and the rectangle defining position and size.

import pygame, sys, os
from pygame.math import Vector2

pygame.init()

cell_size = 30
number_of_cells = 25

SCREEN_WIDTH = cell_size * number_of_cells
SCREEN_HEIGHT = cell_size * number_of_cells

FPS = 60

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Snake Game")

clock = pygame.time.Clock()

class Food:
    def __init__(self):
        # Position in grid cells
        self.position = Vector2(5, 6)
        self.size = cell_size

        # Create a rect for the food based on grid position
        self.rect = pygame.Rect(
            self.position.x * cell_size,
            self.position.y * cell_size,
            self.size,
            self.size
        )

        # Load the food image and scale it to the size of a grid cell (30x30 pixels)
        import os
        script_dir = os.path.dirname(__file__)  # directory where the script is located
        image_path = os.path.join(script_dir, "graphics", "food.png")
        original_surface = pygame.image.load(image_path).convert_alpha()
        self.food_surface = pygame.transform.scale(original_surface, (self.size, self.size))

    def draw(self, surface):
        # Draw the food image onto the screen surface at the rect position
        surface.blit(self.food_surface, self.rect)

def main():
    food = Food()

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill background
        screen.fill(GREEN)

        # Draw food image
        food.draw(screen)

        # Update display and tick clock
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
# Stockdale Assignment 10 - Step 3D: Food Object with Randomized Position
#
# Notes from: https://opal.ils.unc.edu/~lblakej/snake-game/03-add-food/#randomizing-the-food-position
#
# The food object originally appeared in a fixed grid location.
# In this step, the food position is randomized each time the game starts.
#
# A new method generate_random_pos(self) is added to the Food class to generate random x and y
# coordinates within the grid (values from 0 to 24).
#
# These values are used to create a Vector2 object representing the food's position in the grid.
# This method is called inside __init__() to assign a new random position when the food object is created.

import pygame, sys, random
import os
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
        self.size = cell_size

        # Set position using a random grid location
        self.position = self.generate_random_pos()

        # Create a rect for the food based on its position in the grid
        self.rect = pygame.Rect(
            self.position.x * self.size,
            self.position.y * self.size,
            self.size,
            self.size
        )

        # Load the food image and scale it to the size of a grid cell (30x30 pixels)
        script_dir = os.path.dirname(__file__)  # directory where the script is located
        image_path = os.path.join(script_dir, "graphics", "food.png")
        original_surface = pygame.image.load(image_path).convert_alpha()
        self.food_surface = pygame.transform.scale(original_surface, (self.size, self.size))

    def generate_random_pos(self):
        # Generate random x and y values within the grid (0 to 24)
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)

        # Return a new Vector2 position object
        return Vector2(x, y)

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
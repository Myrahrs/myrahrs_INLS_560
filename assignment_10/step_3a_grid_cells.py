# Stockdale Assignment 10 - Step 3A: Create Grid Cells for Positioning
#
# Notes from: https://opal.ils.unc.edu/~lblakej/snake-game/03-add-food/
# Before creating the Food object, I will implement a grid system.
#
# The grid is an invisible division of the game screen into identical cells.
# Each cell acts as a logical space where game objects (like food and snake segments) will be positioned.
#
# This grid simplifies positioning and movement because objects snap to cells instead of arbitrary pixels.
#
# To create the grid, there needs to be two variables:
#
# 1. cell_size: the pixel size of each grid cell (e.g., 30 pixels)
# 2. number_of_cells: how many cells fit in each row and column (e.g., 25 cells)
#
# Since the game screen size will be cell_size * number_of_cells, this gives a 750x750 pixel game window.
# This also means the grid perfectly fits the window without leftover space.
#
# I'll update the screen size to use these expressions to keep things consistent.

import pygame, sys

pygame.init()

# Grid parameters
cell_size = 30                # Size of each grid cell in pixels
number_of_cells = 25          # Number of cells per row and column

# Screen size derived from grid parameters
SCREEN_WIDTH = cell_size * number_of_cells
SCREEN_HEIGHT = cell_size * number_of_cells

FPS = 60

# Colors for background
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Snake Game")

clock = pygame.time.Clock()

def main():
    while True:
        # Event Handling: listen for quit event to close the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill screen with green background color
        screen.fill(GREEN)

        # I could draw the grid lines here for debugging or visualization
        # For now, the grid is invisible and used only logically.

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
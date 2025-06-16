# Stockdale Assignment 10 - Step 4A: Create Snake Body with Rectangles
#
# Notes from: https://opal.ils.unc.edu/~lblakej/snake-game/04-create-snake/
#
# The snake is represented as a list of cells (positions), where each cell is a Vector2 object.
# The first item in the list is the head of the snake.
# The initial snake is three cells long, starting at grid positions:
# Head: (6, 9), Tail: (5, 9), (4, 9)
#
# Each part of the snake is drawn as a DARK_GREEN square on the grid.

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

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Snake Game")

clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        # Snake body is a list of Vector2 positions representing the grid cells
        self.body = [
            Vector2(6, 9),  # Head
            Vector2(5, 9),  # Body
            Vector2(4, 9)   # Tail
        ]

    def draw(self, surface):
        # Draw each segment of the snake as a dark green rectangle
        for segment in self.body:
            x_pos = segment.x * cell_size
            y_pos = segment.y * cell_size
            segment_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(surface, DARK_GREEN, segment_rect)

def main():
    snake = Snake()

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill background
        screen.fill(GREEN)

        # Draw snake body
        snake.draw(screen)

        # Update display and tick clock
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
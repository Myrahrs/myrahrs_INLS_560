# Stockdale Assignment 10 - Step 4B: Make Snake Segments Rounded
#
# Notes from: https://opal.ils.unc.edu/~lblakej/snake-game/04-create-snake/
#
# This step draws the snake with rounded rectangle segments for better visuals.
# Each segment is still a cell on the 25x25 grid, but instead of sharp corners,
# we use a border-radius when drawing.

import pygame, sys, random
from pygame.math import Vector2
import os

# Initialize pygame
pygame.init()

# Grid and screen setup
cell_size = 30
number_of_cells = 25
SCREEN_WIDTH = cell_size * number_of_cells
SCREEN_HEIGHT = cell_size * number_of_cells

# Colors
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

# Frame rate
FPS = 60

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Snake Game")
clock = pygame.time.Clock()

class Food:
    def __init__(self):
        self.size = cell_size
        self.position = self.generate_random_pos()
        self.rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, self.size, self.size)

        # Load and scale the image
        script_dir = os.path.dirname(__file__)
        image_path = os.path.join(script_dir, "graphics", "food.png")
        original_surface = pygame.image.load(image_path).convert_alpha()
        self.food_surface = pygame.transform.scale(original_surface, (self.size, self.size))

    def generate_random_pos(self):
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)
        return Vector2(x, y)

    def draw(self, surface):
        surface.blit(self.food_surface, self.rect)

class Snake:
    def __init__(self):
        # Define initial body with 3 segments
        self.body = [
            Vector2(6, 9),  # Head
            Vector2(5, 9),  # Body
            Vector2(4, 9)   # Tail
        ]

    def draw(self, surface):
        for segment in self.body:
            x = segment.x * cell_size
            y = segment.y * cell_size
            segment_rect = pygame.Rect(x, y, cell_size, cell_size)
            # Rounded rectangle with border_radius=7
            pygame.draw.rect(surface, DARK_GREEN, segment_rect, border_radius=7)

def main():
    food = Food()
    snake = Snake()

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Drawing section
        screen.fill(GREEN)
        food.draw(screen)
        snake.draw(screen)

        # Update screen and control frame rate
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
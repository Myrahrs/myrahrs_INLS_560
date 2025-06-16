# Stockdale Assignment 10 – Step 5B: Move Snake (NO immediate reverse)
#
# This step improves on 5A by **blocking 180‑degree turns**.  
# If the snake is moving right, pressing LEFT is ignored (same for other axes).
#
# Key idea → Only accept a new direction if it is **not** the exact opposite
# of the current direction.  Compare the incoming Vector2 with –self.direction.

import pygame
import sys
import random
from pygame.math import Vector2
import os

# Game configuration
CELL_SIZE = 30
NUM_CELLS = 25
SCREEN_WIDTH = CELL_SIZE * NUM_CELLS
SCREEN_HEIGHT = CELL_SIZE * NUM_CELLS
FPS = 60

# Colors
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Snake Game")
clock = pygame.time.Clock()

# Custom event to update snake position every 200ms
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)


class Food:
    """Food object that spawns randomly on the grid."""
    def __init__(self):
        self.size = CELL_SIZE
        self.position = self._rand_pos()

        # Create a rectangle for positioning
        self.rect = pygame.Rect(
            self.position.x * CELL_SIZE,
            self.position.y * CELL_SIZE,
            self.size,
            self.size
        )

        # Load and scale the food image
        path = os.path.join(os.path.dirname(__file__), "graphics", "food.png")
        img = pygame.image.load(path).convert_alpha()
        self.surface = pygame.transform.scale(img, (self.size, self.size))

    @staticmethod
    def _rand_pos():
        """Generate a random position on the grid."""
        return Vector2(
            random.randint(0, NUM_CELLS - 1),
            random.randint(0, NUM_CELLS - 1)
        )

    def draw(self, surf):
        """Draw the food on the screen."""
        surf.blit(self.surface, self.rect)


class Snake:
    """Snake object made up of a list of Vector2 segments."""
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)  # Initial movement is to the right

    def update(self):
        """Move the snake by adding a new head and removing the tail."""
        self.body = self.body[:-1]  # Remove the last segment (tail)
        self.body.insert(0, self.body[0] + self.direction)  # Add new head

    def set_direction(self, new_dir):
        """Change direction if it's not a 180° turn."""
        if new_dir != -self.direction:
            self.direction = new_dir

    def draw(self, surf):
        """Draw each segment of the snake."""
        for segment in self.body:
            rect = pygame.Rect(
                segment.x * CELL_SIZE,
                segment.y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(surf, DARK_GREEN, rect, border_radius=7)


def main():
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle arrow key input and update snake direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.set_direction(Vector2(0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.set_direction(Vector2(0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.set_direction(Vector2(-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.set_direction(Vector2(1, 0))

            # Move the snake at regular intervals
            if event.type == SNAKE_UPDATE:
                snake.update()

        # Drawing section
        screen.fill(GREEN)
        food.draw(screen)
        snake.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()

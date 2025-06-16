# Stockdale Assignment 10 – Step 5C: Introduce a Game Class
# This step refactors the program so that **one Game object** owns everything:
# `Snake` – handles its own movement and drawing  
# `Food`  – spawns randomly and draws itself  
# `Game`  – orchestrates update / draw logic and will later add collisions, scoring, etc.
# Structure
# Game.update()     -> moves the snake (and later other logic)  
# Game.draw(surface)-> draws food, then snake  
# The main loop now talks **only to the Game object**, keeping `__main__`
# clean and ready for future expansion.


import pygame
import sys
import random
from pygame.math import Vector2
import os

# Grid / screen settings
CELL_SIZE  = 30
NUM_CELLS  = 25
WIDTH      = CELL_SIZE * NUM_CELLS
HEIGHT     = CELL_SIZE * NUM_CELLS
FPS        = 60

# Colours
GREEN      = (173, 204, 96)
DARK_GREEN = (43,  51, 24)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Snake Game")
clock = pygame.time.Clock()

# Custom timer – move the snake every 200 ms
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)


class Food:
    """Single food item that appears at a random grid cell."""
    def __init__(self):
        self.size = CELL_SIZE
        self.position = self._random_cell()
        self.rect = pygame.Rect(
            self.position.x * CELL_SIZE,
            self.position.y * CELL_SIZE,
            self.size,
            self.size
        )
        # Load and scale food image
        img_path = os.path.join(os.path.dirname(__file__), "graphics", "food.png")
        raw = pygame.image.load(img_path).convert_alpha()
        self.surface = pygame.transform.scale(raw, (self.size, self.size))

    @staticmethod
    def _random_cell() -> Vector2:
        x = random.randint(0, NUM_CELLS - 1)
        y = random.randint(0, NUM_CELLS - 1)
        return Vector2(x, y)

    def draw(self, target):
        target.blit(self.surface, self.rect)


class Snake:
    """Snake represented by a list of Vector2 body segments."""
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)   # start moving right

    def update(self):
        """Move one cell in the current direction."""
        self.body = self.body[:-1]                    # drop tail
        self.body.insert(0, self.body[0] + self.direction)

    def set_direction(self, new_dir: Vector2):
        """Change direction unless it is the exact opposite."""
        if new_dir != -self.direction:
            self.direction = new_dir

    def draw(self, target):
        for segment in self.body:
            rect = pygame.Rect(
                segment.x * CELL_SIZE,
                segment.y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(target, DARK_GREEN, rect, border_radius=7)


class Game:
    """Central class that owns all game objects and logic."""
    def __init__(self):
        self.snake = Snake()
        self.food  = Food()

    def update(self):
        """Advance game state: currently only moves the snake."""
        self.snake.update()
        # Future: check collisions, grow snake, spawn new food, etc.

    def draw(self, target):
        """Draw all game objects to the provided surface."""
        self.food.draw(target)
        self.snake.draw(target)


def main():
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Arrow‑key input → propose new direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.snake.set_direction(Vector2(0, -1))
                elif event.key == pygame.K_DOWN:
                    game.snake.set_direction(Vector2(0, 1))
                elif event.key == pygame.K_LEFT:
                    game.snake.set_direction(Vector2(-1, 0))
                elif event.key == pygame.K_RIGHT:
                    game.snake.set_direction(Vector2(1, 0))

            # Timer tick → move the snake
            if event.type == SNAKE_UPDATE:
                game.update()

        # Rendering
        screen.fill(GREEN)
        game.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()

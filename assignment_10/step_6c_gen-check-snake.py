# Stockdale Assignment 10 – Step 6C: Safe Food Spawn (avoid snake body)
#
# When food respawns it must NOT appear on any cell occupied by the snake.
# Food.randomize(snake_body) keeps rolling random cells until safe.

import pygame
import sys
import random
from pygame.math import Vector2
import os

# basic setup
CELL_SIZE, NUM_CELLS = 30, 25
WIDTH, HEIGHT = CELL_SIZE * NUM_CELLS, CELL_SIZE * NUM_CELLS
GREEN, DARK_GREEN = (173, 204, 96), (43, 51, 24)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Snake Game")
clock = pygame.time.Clock()

# custom timer to move snake every 200 ms
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)


class Food:
    def __init__(self):
        self.size = CELL_SIZE
        img_path = os.path.join(os.path.dirname(__file__), "graphics", "food.png")
        raw = pygame.image.load(img_path).convert_alpha()
        self.surface = pygame.transform.scale(raw, (self.size, self.size))
        self.position = Vector2()          # placeholder
        self.randomize([])                 # safe first spawn (no snake yet)

    @staticmethod
    def _rand_cell():
        return Vector2(
            random.randint(0, NUM_CELLS - 1),
            random.randint(0, NUM_CELLS - 1)
        )

    def randomize(self, snake_body):
        """Pick a random grid cell NOT contained in snake_body."""
        self.position = self._rand_cell()
        while self.position in snake_body:
            self.position = self._rand_cell()

        self.rect = pygame.Rect(
            self.position.x * CELL_SIZE,
            self.position.y * CELL_SIZE,
            self.size,
            self.size
        )

    def draw(self, surf):
        surf.blit(self.surface, self.rect)


class Snake:
    """Same snake as previous step, with grow‑flag logic."""
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
        self.add_segment = False

    def update(self):
        new_head = self.body[0] + self.direction
        if not self.add_segment:
            self.body = self.body[:-1]      # drop tail (normal move)
        else:
            self.add_segment = False        # consume growth flag (not used now)
        self.body.insert(0, new_head)       # add new head

    def set_direction(self, new_dir):
        if new_dir != -self.direction:      # block 180‑turns
            self.direction = new_dir

    def draw(self, surf):
        for seg in self.body:
            rect = pygame.Rect(
                seg.x * CELL_SIZE,
                seg.y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(surf, DARK_GREEN, rect, border_radius=7)


class Game:
    """Owns snake + food and handles collision logic."""
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def update(self):
        self.snake.update()
        self.check_eat_food()

    def check_eat_food(self):
        if self.snake.body[0] == self.food.position:
            # Removed growth trigger so snake does NOT grow
            # self.snake.add_segment = True  # <-- comment this out or delete
            
            # respawn food, avoiding current snake cells
            self.food.randomize(self.snake.body)

    def draw(self, surf):
        self.food.draw(surf)
        self.snake.draw(surf)


def main():
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.snake.set_direction(Vector2(0, -1))
                elif event.key == pygame.K_DOWN:
                    game.snake.set_direction(Vector2(0, 1))
                elif event.key == pygame.K_LEFT:
                    game.snake.set_direction(Vector2(-1, 0))
                elif event.key == pygame.K_RIGHT:
                    game.snake.set_direction(Vector2(1, 0))

            if event.type == SNAKE_UPDATE:
                game.update()

        screen.fill(GREEN)
        game.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
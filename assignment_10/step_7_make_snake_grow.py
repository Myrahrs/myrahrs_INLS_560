# Stockdale Assignment 10 – Step 7: Make Snake Grow
#
# When the snake eats food, it grows by adding a new segment
# to its body instead of moving (which normally removes the tail).
# This is done by using an `add_segment` flag in the Snake class.

import pygame, sys, random, os
from pygame.math import Vector2

# Basic setup
CELL_SIZE, NUM_CELLS = 30, 25
WIDTH, HEIGHT = CELL_SIZE * NUM_CELLS, CELL_SIZE * NUM_CELLS
GREEN, DARK_GREEN = (173, 204, 96), (43, 51, 24)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Snake Game")
clock = pygame.time.Clock()

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

# Helper classes

class Food:
    def __init__(self):
        self.size = CELL_SIZE
        img_path = os.path.join(os.path.dirname(__file__), "graphics", "food.png")
        raw = pygame.image.load(img_path).convert_alpha()
        self.surface = pygame.transform.scale(raw, (self.size, self.size))
        self.position = Vector2()
        self.randomize([])  # start with empty snake

    @staticmethod
    def _rand_cell():
        return Vector2(random.randint(0, NUM_CELLS - 1),
                       random.randint(0, NUM_CELLS - 1))

    def randomize(self, snake_body):
        # Place food somewhere not occupied by snake
        self.position = self._rand_cell()
        while self.position in snake_body:
            self.position = self._rand_cell()
        self.rect = pygame.Rect(self.position.x * CELL_SIZE,
                                self.position.y * CELL_SIZE,
                                self.size, self.size)

    def draw(self, surf):
        surf.blit(self.surface, self.rect)


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.add_segment = False  # Flag to grow snake

    def update(self):
        new_head = self.body[0] + self.direction

        if self.add_segment:
            # When adding segment, don't remove tail (snake grows)
            self.add_segment = False  # Reset flag after growing
        else:
            # Normal move: remove last segment (tail)
            self.body.pop()

        # Insert new head at front
        self.body.insert(0, new_head)

    def set_direction(self, direction):
        # Optional: prevent snake from reversing direction
        if (direction + self.direction) != Vector2(0, 0):
            self.direction = direction

    def draw(self, surf):
        for segment in self.body:
            rect = pygame.Rect(segment.x * CELL_SIZE,
                               segment.y * CELL_SIZE,
                               CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surf, DARK_GREEN, rect)
            pygame.draw.rect(surf, GREEN, rect.inflate(-4, -4))


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def update(self):
        self.snake.update()
        self.check_eat_food()

    def check_eat_food(self):
        # Check if snake head is on food
        if self.snake.body[0] == self.food.position:
            # Tell snake to grow next update cycle
            self.snake.add_segment = True

            # Reposition food, avoid snake body
            self.food.randomize(self.snake.body)

    def draw(self, surf):
        self.food.draw(surf)
        self.snake.draw(surf)


def main():
    game = Game()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    game.snake.set_direction(Vector2(0, -1))
                elif e.key == pygame.K_DOWN:
                    game.snake.set_direction(Vector2(0, 1))
                elif e.key == pygame.K_LEFT:
                    game.snake.set_direction(Vector2(-1, 0))
                elif e.key == pygame.K_RIGHT:
                    game.snake.set_direction(Vector2(1, 0))
            if e.type == SNAKE_UPDATE:
                game.update()

        screen.fill(GREEN)
        game.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
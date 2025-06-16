# Stockdale Assignment 10 – Step 5A: Move Snake (reverse allowed)
#
# Notes (source: https://opal.ils.unc.edu/~lblakej/snake-game/05-move-snake/)
# --------------------------------------------------------------------------
#  The snake is a list of Vector2 grid‑coordinates.  
#  “Moving” the snake means:
#    1. Remove the last list element (tail) → self.body = self.body[:-1]
#    2. Insert a new head at index 0 that is one cell in the current direction.  
#  Direction is stored as a Vector2.  (1, 0)=right, (‑1, 0)=left, (0, ‑1)=up, (0, 1)=down  
#  A pygame **timer event** (SNAKE_UPDATE) fires every 200 ms so the snake
#   moves at a playable speed instead of 60 cells / sec.  
#  Keyboard handling (arrow keys) sets self.direction.  
#   **This “yes‑reverse” version allows 180‑degree turns.**
# --------------------------------------------------------------------------

import pygame, sys, random
from pygame.math import Vector2
import os

pygame.init()

# grid / screen  
CELL_SIZE        = 30
NUM_CELLS        = 25
SCREEN_WIDTH     = CELL_SIZE * NUM_CELLS
SCREEN_HEIGHT    = CELL_SIZE * NUM_CELLS

#  colors
GREEN      = (173, 204,  96)
DARK_GREEN = ( 43,  51,  24)

# Pygame init
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Snake Game")
clock  = pygame.time.Clock()
FPS    = 60                              # render speed

# Custom timer event: move snake every 200 ms
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)  # 200 ms interval

# classes
class Food:
    """Food appears at a random grid position and is drawn from an image."""
    def __init__(self):
        self.size     = CELL_SIZE
        self.position = self.random_pos()
        self.rect     = pygame.Rect(self.position.x * CELL_SIZE,
                                    self.position.y * CELL_SIZE,
                                    self.size, self.size)
        # load + scale image
        script_dir   = os.path.dirname(__file__)
        img_path     = os.path.join(script_dir, "graphics", "food.png")
        original_sfc = pygame.image.load(img_path).convert_alpha()
        self.surface = pygame.transform.scale(original_sfc, (self.size, self.size))

    def random_pos(self) -> Vector2:
        x = random.randint(0, NUM_CELLS - 1)
        y = random.randint(0, NUM_CELLS - 1)
        return Vector2(x, y)

    def draw(self, target):
        target.blit(self.surface, self.rect)

class Snake:
    """3‑segment snake that can move one cell per timer tick."""
    def __init__(self):
        self.body = [Vector2(6, 9),
                     Vector2(5, 9),
                     Vector2(4, 9)]
        self.direction = Vector2(1, 0)   # start moving right

    # movement logic
    def update(self):
        # drop tail …
        self.body = self.body[:-1]
        # … and add new head = old head + direction
        new_head  = self.body[0] + self.direction
        self.body.insert(0, new_head)

    #  drawing logic
    def draw(self, target):
        for segment in self.body:
            rect = pygame.Rect(segment.x * CELL_SIZE,
                               segment.y * CELL_SIZE,
                               CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(target, DARK_GREEN, rect, border_radius=7)

#  main loop
def main():
    snake = Snake()
    food  = Food()

    while True:
        # ─ event handling ─
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            # arrow keys → set direction  (reverse allowed in this step)
            if event.type == pygame.KEYDOWN:
                if   event.key == pygame.K_UP:    snake.direction = Vector2( 0, -1)
                elif event.key == pygame.K_DOWN:  snake.direction = Vector2( 0,  1)
                elif event.key == pygame.K_LEFT:  snake.direction = Vector2(-1,  0)
                elif event.key == pygame.K_RIGHT: snake.direction = Vector2( 1,  0)

            # custom timer event → move snake
            if event.type == SNAKE_UPDATE:
                snake.update()

        # ─ drawing ─
        screen.fill(GREEN)
        food.draw(screen)
        snake.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
# Stockdale Assignment 10 – Step 6B: Refactor Food Position Generator
#
# Adds Food.generate_random_pos() to centralize random‑cell creation.
# Behavior is unchanged (food can still spawn on the snake).

import pygame, sys, random, os
from pygame.math import Vector2

#  basic setup 
CELL_SIZE, NUM_CELLS = 30, 25
WIDTH, HEIGHT        = CELL_SIZE * NUM_CELLS, CELL_SIZE * NUM_CELLS
GREEN, DARK_GREEN    = (173, 204, 96), (43, 51, 24)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Snake Game")
clock = pygame.time.Clock()

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

# helper classes 
# Food class changes to include random position
class Food:
    def __init__(self):
        self.size = CELL_SIZE
        self.position = self.generate_random_pos()
        self._update_rect()

        img_path = os.path.join(os.path.dirname(__file__), "graphics", "food.png")
        raw = pygame.image.load(img_path).convert_alpha()
        self.surface = pygame.transform.scale(raw, (self.size, self.size))

    @staticmethod
    def generate_random_pos():
        """Return a random Vector2 inside the grid."""
        return Vector2(random.randint(0, NUM_CELLS-1),
                       random.randint(0, NUM_CELLS-1))

    def _update_rect(self):
        self.rect = pygame.Rect(self.position.x * CELL_SIZE,
                                self.position.y * CELL_SIZE,
                                self.size, self.size)

    def randomize(self):
        self.position = self.generate_random_pos()
        self._update_rect()

    def draw(self, target): target.blit(self.surface, self.rect)

# Snake, Game, and main loop remain exactly the same as Step 6A
class Snake:
    def __init__(self):
        self.body        = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction   = Vector2(1,0)
        self.add_segment = False

    def update(self):
        new_head = self.body[0] + self.direction
        if not self.add_segment:
            self.body = self.body[:-1]            # drop tail only when not growing
        else:
            self.add_segment = False              # consume growth flag
        self.body.insert(0, new_head)             # add new head

    def set_direction(self, new_dir):
        if new_dir != -self.direction:            # block 180‑turns
            self.direction = new_dir

    def draw(self, surf):
        for seg in self.body:
            rect = pygame.Rect(seg.x*CELL_SIZE, seg.y*CELL_SIZE,
                               CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surf, DARK_GREEN, rect, border_radius=7)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food  = Food()

    def update(self):
        self.snake.update()
        self.check_eat_food()

    def check_eat_food(self):
        if self.snake.body[0] == self.food.position:
            #self.snake.add_segment = True
            self.food.randomize()                 # may land on snake (fixed later)

    def draw(self, surf):
        self.food.draw(surf)
        self.snake.draw(surf)

#  main loop 
def main():
    game = Game()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if   e.key == pygame.K_UP:    game.snake.set_direction(Vector2(0,-1))
                elif e.key == pygame.K_DOWN:  game.snake.set_direction(Vector2(0, 1))
                elif e.key == pygame.K_LEFT:  game.snake.set_direction(Vector2(-1,0))
                elif e.key == pygame.K_RIGHT: game.snake.set_direction(Vector2(1, 0))
            if e.type == SNAKE_UPDATE: game.update()

        screen.fill(GREEN)
        game.draw(screen)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
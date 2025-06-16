# Stockdale Assignment 10 - Step 1B: Game Loop (Black Background)
# 
# Notes for this step from : https://opal.ils.unc.edu/~lblakej/snake-game/02b-game-loop/
# The game loop is responsible for updating game objects and checking for collisions.
# It runs repeatedly until the game is closed.
#
# Each iteration of the game loop has three essential steps:
# 1. Event Handling: Detect events like quitting or key presses.
# 2. Updating Positions: Update positions of all game objects.
# 3. Drawing Objects: Draw all game objects on the screen.
#
# The while loop runs continuously:
#   while True:
# This runs the three steps at each iteration.
#
# Event handling uses pygame.event.get() to get all events.
# If the user clicks the close button (QUIT event), we exit the loop and close the program.
#
# pygame.display.update() updates the screen with all changes.
#
# clock.tick(FPS) controls how fast the loop runs, here 60 frames per second.
# This keeps the game running smoothly at a consistent speed.
#
# At this step, the screen is filled with black color.

import pygame, sys

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Snake Game")

clock = pygame.time.Clock()

def main():
    while True:
        # Event Handling: check for any events (like closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Drawing Objects: fill the screen with black (background color)
        screen.fill((0, 0, 0))  # RGB for black

        # Update the display with everything drawn so far
        pygame.display.update()

        # Control the frame rate to 60 FPS
        clock.tick(FPS)

if __name__ == "__main__":
    main()

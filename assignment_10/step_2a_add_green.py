# Stockdale Assignment 10 - Step 2A: Add Green Background
#
# Notes from : https://opal.ils.unc.edu/~lblakej/snake-game/02b-game-loop/#make-game-window-green
# Now we will change the black background to green to create a retro look.
#
# Colors in Pygame are defined by RGB tuples.
# We'll define two green shades:
# - GREEN (173, 204, 96) for the main background
# - DARK_GREEN (43, 51, 24) can be used later for accents or grid
#
# The fill() method paints the entire screen with the given color.
#
# Running this will show a green game window.
#
# Everything else (game loop and event handling) remains the same.

import pygame, sys

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Snake Game")

clock = pygame.time.Clock()

# Define green colors for retro look
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

def main():
    while True:
        # Event Handling: listen for quit event to close game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Drawing Objects: fill screen with green background color
        screen.fill(GREEN)

        # Update the display with the new drawing
        pygame.display.update()

        # Control frame rate to 60 FPS
        clock.tick(FPS)

if __name__ == "__main__":
    main()

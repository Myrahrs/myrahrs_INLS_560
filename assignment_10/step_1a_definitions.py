# Stockdale Assignment 10 - Step 1A
import pygame

# Initialize Pygame library to start using all its modules (graphics, sound, input, etc.)
pygame.init()

# Constants for the game window dimensions and frame rate
SCREEN_WIDTH = 750  # Width of the game window in pixels
SCREEN_HEIGHT = 750 # Height of the game window in pixels
FPS = 15  # Frames per second — controls how fast the game updates (speed)

# Set up the display window with specified width and height
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the caption/title of the game window
pygame.display.set_caption("Retro Snake Game")

# Create a clock object to help control the frame rate (game speed)
clock = pygame.time.Clock()

# Define some common colors as RGB tuples for easy reference
WHITE = (255, 255, 255)  # White color
BLACK = (0, 0, 0)        # Black color (background)
GREEN = (0, 255, 0)      # Green color (snake color)

# Define the Snake class that will manage snake properties and behavior
class Snake:
    def __init__(self):
        """
        Constructor method runs automatically when creating a new Snake object.
        Sets initial position, size, and body segments.
        """
        # Start the snake roughly in the center of the screen
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2

        # Each segment of the snake will be a 20x20 pixel square
        self.size = 20  

        # The snake body is a list of (x, y) tuples representing each segment's position
        # Initially, the snake has only one segment at the starting position
        self.body = [(self.x, self.y)]

    def draw(self, surface):
        """
        Draws the snake on the given surface (screen).
        Iterates through each segment and draws a green rectangle.
        """
        for segment in self.body:
            # Draw a rectangle at each segment's position with size self.size
            pygame.draw.rect(surface, GREEN, (*segment, self.size, self.size))

# Main function where the game loop runs and events are processed
def main():
    running = True           # Flag to keep the game running
    snake = Snake()          # Create an instance of the Snake class

    # Game loop: runs continuously until 'running' is set to False
    while running:
        # Event handling: check all events that happen (keyboard, mouse, window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user closes the window
                running = False             # Exit the game loop

        # Fill the screen with black to clear previous drawings
        screen.fill(BLACK)

        # Draw the snake on the screen
        snake.draw(screen)

        # Update the display to show the new frame
        pygame.display.update()

        # Tick the clock to enforce the frame rate (FPS)
        clock.tick(FPS)

    # When the game loop ends, quit pygame cleanly
    pygame.quit()

# Ensure this file runs the main function only if executed directly
if __name__ == "__main__":
    main()

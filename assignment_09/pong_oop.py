# This is a Python Pong game with Object Oriented Programming.
import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 800

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Frame rate
FPS = 60

# Speeds
PADDLE_SPEED = 7
BALL_SPEED_X, BALL_SPEED_Y = 5, 5


class Paddle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = PADDLE_SPEED

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)


class Ball:
    def __init__(self, x, y, radius):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.dx = BALL_SPEED_X
        self.dy = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Bounce off top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy = -self.dy

    def reset(self, x, y):
        self.rect.center = (x, y)
        self.dx = -self.dx  # Reverse direction on reset

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)


class PongGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong Game (OOP Version)")

        self.clock = pygame.time.Clock()

        # Initialize paddles and ball
        self.left_paddle = Paddle(10, (HEIGHT - 100) // 2, 10, 100)
        self.right_paddle = Paddle(WIDTH - 20, (HEIGHT - 100) // 2, 10, 100)
        self.ball = Ball(WIDTH // 2, HEIGHT // 2, 7)

        # Scores
        self.left_score = 0
        self.right_score = 0

        # Font for displaying scores
        self.font = pygame.font.Font(None, 74)

    def draw_scores(self):
        left_text = self.font.render(str(self.left_score), True, WHITE)
        right_text = self.font.render(str(self.right_score), True, WHITE)
        self.screen.blit(left_text, (WIDTH // 4, 20))
        self.screen.blit(right_text, (WIDTH * 3 // 4, 20))

    def handle_collisions(self):
        # Ball collision with paddles
        if self.ball.rect.colliderect(self.left_paddle.rect) or self.ball.rect.colliderect(self.right_paddle.rect):
            self.ball.dx = -self.ball.dx

        # Ball out of bounds
        if self.ball.rect.left <= 0:
            self.right_score += 1
            self.ball.reset(WIDTH // 2, HEIGHT // 2)

        if self.ball.rect.right >= WIDTH:
            self.left_score += 1
            self.ball.reset(WIDTH // 2, HEIGHT // 2)

    def run(self):
        while True:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Paddle movement
            self.left_paddle.move(pygame.K_w, pygame.K_s)
            self.right_paddle.move(pygame.K_UP, pygame.K_DOWN)

            # Ball movement
            self.ball.move()

            # Handle collisions
            self.handle_collisions()

            # Drawing everything
            self.screen.fill(BLACK)
            self.left_paddle.draw(self.screen)
            self.right_paddle.draw(self.screen)
            self.ball.draw(self.screen)
            self.draw_scores()
            pygame.draw.aaline(self.screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

            # Update display
            pygame.display.flip()

            # Frame rate
            self.clock.tick(FPS)


if __name__ == "__main__":
    PongGame().run()
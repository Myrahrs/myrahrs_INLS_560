# Stockdale - Motorcross game.

import pygame        # Library for game development (graphics, input, sound)
import os            # Operating system utilities (file paths, directory handling)
import time          # Time-related functions (delays, timestamps)
import random        # Random number generation (for variability in game behavior)
import math          # Mathematical functions (trigonometry, needed for oval track calculations)

pygame.init()        # Initialize all imported pygame modules (required before using pygame features)

# Screen setup.
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Motorcross Game")

# Fonts.
FONT_LARGE = pygame.font.SysFont('arial', 72)
FONT_MEDIUM = pygame.font.SysFont('arial', 36)
FONT_SMALL = pygame.font.SysFont('arial', 24)

# Colors.
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
TRACK_COLOR = (80, 80, 80)
INNER_TRACK_COLOR = (50, 50, 50)

# Path to motorbike image with transparent background.
MOTORBIKE_IMG_PATH = os.path.join("assignment_09", "Motorcross_Game", "motorbike2.png")

# Number of laps
TOTAL_LAPS = 3
TRACK_WIDTH = 80

clock = pygame.time.Clock()

# OOP: Define Racer class.
class Racer:
    def __init__(self, name):
        self.name = name
        self.progress = 0.0
        self.speed = 0.0017 + random.uniform(0, 0.0008)
        self.laps = 0
        self.finished = False
        self.finish_time = None
        self.color = self.random_color()

        # Load, scale, and tint the motorbike icon.
        base_img = pygame.image.load(MOTORBIKE_IMG_PATH).convert_alpha()
        base_img = pygame.transform.scale(base_img, (50, 50))
        self.icon = self.tint_image(base_img, self.color)

    def random_color(self):
        return (
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255)
        )

    def tint_image(self, image, tint_color):
        """Apply a color overlay to the image."""
        tinted = image.copy()
        tint_surface = pygame.Surface(tinted.get_size(), pygame.SRCALPHA)
        tint_surface.fill(tint_color + (0,))  # Keep alpha
        tinted.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return tinted

def draw_text_center(text, font, color, surface, y):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(WIDTH // 2, y))
    surface.blit(rendered, rect)

def get_racers_input():
    racers = []
    input_text = ""
    input_active = True
    clock_input = pygame.time.Clock()

    while input_active:
        screen.fill(BG_COLOR)
        prompt_text = (
            "Enter racer names (Press ENTER after each; "
            "Press ESC when all racers are input)"
        )
        draw_text_center(prompt_text, FONT_MEDIUM, TEXT_COLOR, screen, HEIGHT // 4)

        input_surface = FONT_MEDIUM.render(input_text, True, TEXT_COLOR)
        input_rect = input_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(input_surface, input_rect)

        y_offset = HEIGHT // 2 + 50
        for racer in racers:
            racer_text = FONT_SMALL.render(racer.name, True, TEXT_COLOR)
            screen.blit(racer_text, (WIDTH // 2 - racer_text.get_width() // 2, y_offset))
            y_offset += 30

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.strip():
                        racers.append(Racer(input_text.strip()))
                        input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and racers:
            input_active = False

        clock_input.tick(30)

    return racers

def countdown():
    for num in ["3", "2", "1", "GO!"]:
        screen.fill(BG_COLOR)
        text = FONT_LARGE.render(num, True, TEXT_COLOR)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(1)

# Generate an oval track.
def generate_oval_track(cx, cy, rx, ry, points_count=400):
    return [(cx + rx * math.cos(2 * math.pi * i / points_count),
             cy + ry * math.sin(2 * math.pi * i / points_count))
            for i in range(points_count)]

def draw_oval_track(outer_points, inner_points):
    pygame.draw.polygon(screen, TRACK_COLOR, outer_points)
    pygame.draw.polygon(screen, INNER_TRACK_COLOR, inner_points)

def get_track_position(outer_points, inner_points, progress):
    idx = int(progress * len(outer_points)) % len(outer_points)
    x = (outer_points[idx][0] + inner_points[idx][0]) / 2
    y = (outer_points[idx][1] + inner_points[idx][1]) / 2
    return int(x), int(y)

def display_timer_and_lap(elapsed_ms, current_lap, total_laps):
    elapsed_sec = elapsed_ms / 1000
    timer_text = f"Time: {elapsed_sec:.2f}s"
    lap_text = f"Lap: {current_lap}/{total_laps}"

    rect = pygame.Surface((220, 70), pygame.SRCALPHA)
    rect.fill((0, 0, 0, 180))
    screen.blit(rect, ((WIDTH - 220) // 2, 10))

    timer_surface = FONT_MEDIUM.render(timer_text, True, TEXT_COLOR)
    lap_surface = FONT_MEDIUM.render(lap_text, True, TEXT_COLOR)
    screen.blit(timer_surface, ((WIDTH - timer_surface.get_width()) // 2, 15))
    screen.blit(lap_surface, ((WIDTH - lap_surface.get_width()) // 2, 45))

def display_winners(racers):
    screen.fill(BG_COLOR)
    draw_text_center("Race Results", FONT_LARGE, TEXT_COLOR, screen, HEIGHT // 6)

    sorted_racers = sorted(
        [r for r in racers if r.finish_time is not None],
        key=lambda r: r.finish_time
    )

    for i, racer in enumerate(sorted_racers[:3]):
        text = f"{i+1}. {racer.name} - {racer.finish_time / 1000:.2f}s"
        draw_text_center(text, FONT_MEDIUM, TEXT_COLOR, screen, HEIGHT // 3 + i * 50)

    pygame.display.flip()
    time.sleep(7)

# Main game loop.
def main():
    racers = get_racers_input()
    countdown()

    cx, cy = WIDTH // 2, HEIGHT // 2 + 50
    outer = generate_oval_track(cx, cy, 350, 200)
    inner = generate_oval_track(cx, cy, 350 - TRACK_WIDTH, 200 - TRACK_WIDTH)

    start_ticks = pygame.time.get_ticks()
    finish_order = []
    race_finished = False

    while True:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        draw_oval_track(outer, inner)

        current_time = pygame.time.get_ticks()
        elapsed = current_time - start_ticks

        if not race_finished:
            for racer in racers:
                if not racer.finished:
                    racer.progress += racer.speed
                    if racer.progress >= 1.0:
                        racer.progress -= 1.0
                        racer.laps += 1
                        if racer.laps >= TOTAL_LAPS:
                            racer.finished = True
                            racer.finish_time = current_time - start_ticks
                            finish_order.append(racer)

            if all(r.finished for r in racers):
                race_finished = True

            max_lap = max(r.laps for r in racers)
            display_timer_and_lap(elapsed, min(max_lap + 1, TOTAL_LAPS), TOTAL_LAPS)

        for racer in racers:
            x, y = get_track_position(outer, inner, racer.progress)
            screen.blit(racer.icon, (x - 25, y - 25))
            name_surface = FONT_SMALL.render(racer.name, True, TEXT_COLOR)
            screen.blit(name_surface, (x - name_surface.get_width() // 2, y + 30))

        if race_finished:
            display_winners(racers)
            return

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
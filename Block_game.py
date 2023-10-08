import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
RED_COLOR = (255, 0, 0)
RED_SIZE = 20  # Smaller red square size
GREEN_COLOR = (0, 255, 0)
GREEN_SIZE = 40  # Larger green square size
BOUNDARY_COLOR = (0, 0, 0)
BOUNDARY_WIDTH = 10

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Puzzle Game")

# Initial position of the red square
red_x, red_y = 20, HEIGHT // 2 - RED_SIZE // 2

# Initial position of the green square (target)
green_x, green_y = WIDTH - 60, HEIGHT // 2 - GREEN_SIZE // 2

# Game loop
running = True
completed = False
completion_time = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Get the position of the mouse cursor
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw the green square (target)
    pygame.draw.rect(screen, GREEN_COLOR, (green_x, green_y, GREEN_SIZE, GREEN_SIZE))

    # Draw the red square
    pygame.draw.rect(screen, RED_COLOR, (red_x, red_y, RED_SIZE, RED_SIZE))

    # Draw boundaries
    pygame.draw.rect(screen, BOUNDARY_COLOR, (0, 0, WIDTH, BOUNDARY_WIDTH))  # Top boundary
    pygame.draw.rect(screen, BOUNDARY_COLOR, (0, 0, BOUNDARY_WIDTH, HEIGHT))  # Left boundary
    pygame.draw.rect(screen, BOUNDARY_COLOR, (0, HEIGHT - BOUNDARY_WIDTH, WIDTH, BOUNDARY_WIDTH))  # Bottom boundary
    pygame.draw.rect(screen, BOUNDARY_COLOR, (WIDTH - BOUNDARY_WIDTH, 0, BOUNDARY_WIDTH, HEIGHT))  # Right boundary

    # Move the red square toward the mouse cursor
    dx, dy = mouse_x - red_x, mouse_y - red_y
    length = (dx ** 2 + dy ** 2) ** 0.5
    if length != 0:
        dx, dy = dx / length, dy / length

    if not completed:
        red_x += dx * 2  # Adjust the speed by changing the multiplier
        red_y += dy * 2

    # Check if the red square overlaps with the green square (target)
    if red_x >= green_x and red_x + RED_SIZE <= green_x + GREEN_SIZE and \
            red_y >= green_y and red_y + RED_SIZE <= green_y + GREEN_SIZE:
        completed = True
        completion_time = time.time()

    if completed:
        font = pygame.font.Font(None, 36)
        text = font.render("Puzzle Completed!", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - 125, HEIGHT // 2 - 50))

        # Check if 2 seconds have passed since completion
        if time.time() - completion_time >= 2:
            running = False

    # Check if the red square touches any boundary
    if (red_x <= BOUNDARY_WIDTH or red_x + RED_SIZE >= WIDTH - BOUNDARY_WIDTH or
            red_y <= BOUNDARY_WIDTH or red_y + RED_SIZE >= HEIGHT - BOUNDARY_WIDTH):
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - 75, HEIGHT // 2 - 50))
        pygame.display.update()
        pygame.time.delay(2000)  # Pause for 2 seconds before quitting
        running = False

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

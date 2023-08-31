import pygame
import random
from bush import Bush, update_bush_lifecycle, generate_bushes
from terrain import Terrain
from tree import Tree, generate_trees, update_tree_lifecycle  # Assuming these are in a file named 'tree.py'


# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Divine Simulation - World for Followers")

# Font for displaying month and year
font = pygame.font.Font(None, 36)

# Time progression
current_month = 1
current_year = 1
month_duration_seconds = 5
time_elapsed = 0

# Initialize terrain and bushes
terrain = Terrain(screen_width, screen_height)
bushes = generate_bushes(terrain.surface, terrain.block_colors)
trees = generate_trees(terrain.surface, terrain.block_colors)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Draw terrain
    screen.blit(terrain.surface, (0, 0))

    # Update time progression
    time_elapsed += clock.tick(30)
    if time_elapsed >= month_duration_seconds * 1000:
        current_month += 1
        time_elapsed = 0

        if current_month > 12:
            current_month = 1
            current_year += 1

        # Update bush life cycle
        update_bush_lifecycle(bushes)

    for tree in trees:
        pygame.draw.circle(screen, (0, 100, 0), (tree.x, tree.y), 10)  

    # Draw bushes and berries
    for bush in bushes:
        pygame.draw.circle(screen, (0, 255, 0), (bush.x, bush.y), 5)
        for berry in bush.berries:
            pygame.draw.circle(screen, (255, 0, 0), berry, 2)

    # Clear the area where the month and year text will be displayed
    pygame.draw.rect(screen, (0, 0, 0), (screen_width - 200, 0, 200, 50))

    # Display current month and year
    month_text = font.render(f"Month: {current_month}, Year: {current_year}", True, (255, 255, 255))
    screen.blit(month_text, (screen_width - month_text.get_width() - 10, 10))

    pygame.display.flip()

# Quit Pygame
pygame.quit()

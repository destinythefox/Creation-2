import pygame
from terrain import generate_terrain
from tree import generate_trees, update_tree_lifecycle
from bush import generate_bushes, update_bush_lifecycle
import random 

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Divine Simulation - World for Followers")

# Generate terrain
terrain = generate_terrain(screen_width, screen_height)

# Generate trees
biome_colors = {
    "grass": (0, 128, 0),
    "stone": (128, 128, 128),
    "water": (0, 0, 255),
    "sand": (255, 255, 102)
}
trees = generate_trees(terrain, biome_colors)

# Generate bushes
bushes = generate_bushes(terrain, biome_colors)

# Time progression
current_month = 1
month_duration_seconds = 5
time_elapsed = 0

# Font for displaying month
font = pygame.font.Font(None, 36)

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

    # Update time progression
    time_elapsed += clock.get_time()  # Get time since last frame in milliseconds
    if time_elapsed >= month_duration_seconds * 1000:
        current_month += 1
        time_elapsed = 0
        
        # Update tree and bush life cycles
        update_tree_lifecycle(trees)
        update_bush_lifecycle(bushes)
    
    screen.blit(terrain, (0, 0))
    
    # Draw trees
    for tree in trees:
        pygame.draw.circle(screen, (0, 255, 0), (tree.x, tree.y), 2)  # Green dots
    
    # Draw bushes with berries
    for bush in bushes:
        pygame.draw.circle(screen, (0, 255, 0), (bush.x, bush.y), 5)  # Green circle
        for _ in range(bush.berries):
            pygame.draw.circle(screen, (255, 0, 0), (bush.x + random.randint(-2, 2), bush.y + random.randint(-2, 2)), 2)  # Red dot
    
    # Display current month
    month_text = font.render("Month: " + str(current_month), True, (255, 255, 255))
    screen.blit(month_text, (screen_width - month_text.get_width() - 10, 10))
        
    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 30 FPS

# Quit Pygame
pygame.quit()

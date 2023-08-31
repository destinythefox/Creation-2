import pygame
import noise

def generate_terrain(width, height):
    terrain = pygame.Surface((width, height))
    
    block_size = 20
    num_blocks_x = width // block_size
    num_blocks_y = height // block_size
    
    block_colors = {
        "grass": (0, 128, 0),  # Green (grass block)
        "stone": (128, 128, 128),  # Gray (stone block)
        "water": (0, 0, 255),  # Blue (water block)
        "sand": (255, 255, 102)  # Light brown (sand block)
    }
    
    scale = 0.1  # Adjust to control terrain variation
    for x in range(num_blocks_x):
        for y in range(num_blocks_y):
            noise_value = noise.pnoise2(x * scale, y * scale)
            
            if noise_value < -0.2:
                block_type = "water"
            elif noise_value < 0:
                block_type = "sand"
            elif noise_value < 0.7:
                block_type = "grass"
            else:
                block_type = "stone"
            
            block_color = block_colors[block_type]
            
            block_rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            pygame.draw.rect(terrain, block_color, block_rect)
            
    return terrain

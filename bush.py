import pygame
import random

class Bush:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.berries = 3  # Initial number of berries
        self.month = 1
        self.month_duration_milliseconds = 5000  # 5 seconds per month

def update_bush_lifecycle(bushes):
    for bush in bushes:
        bush.month += 1
        if bush.month > 12:
            bush.month = 1
            bush.berries = 3

def generate_bushes(terrain_surface, biome_colors):
    bushes = []
    
    num_bushes = 50  # Adjust the number of bushes
    
    for _ in range(num_bushes):
        x = random.randint(0, terrain_surface.get_width() - 1)
        y = random.randint(0, terrain_surface.get_height() - 1)
        
        color_at_position = terrain_surface.get_at((x, y))[:3]  # Get RGB color
        
        # Check if the position is suitable for a bush
        if color_at_position in biome_colors.values() and color_at_position != biome_colors["water"] and color_at_position != biome_colors["sand"]:
            bushes.append(Bush(x, y))
            
    return bushes

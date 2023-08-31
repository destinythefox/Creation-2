import pygame
import noise

class Terrain:
    def __init__(self, width, height, seed):
        self.width = width
        self.height = height
        self.seed = seed
        self.block_colors = {
            "grass": (0, 128, 0),
            "forest": (0, 100, 0),  # Darker green for forest
            "stone": (128, 128, 128),
            "water": (0, 0, 255),
            "sand": (255, 255, 102)
        }
        self.surface = self.generate_terrain()

    def generate_terrain(self):
        terrain = pygame.Surface((self.width, self.height))
        block_size = 20
        num_blocks_x = self.width // block_size
        num_blocks_y = self.height // block_size
        scale = 0.1
        for x in range(num_blocks_x):
            for y in range(num_blocks_y):
                noise_value = noise.pnoise2(x * scale + self.seed, y * scale + self.seed)
                if noise_value < -0.2:
                    block_type = "water"
                elif noise_value < 0:
                    block_type = "sand"
                elif noise_value < 0.7:
                    block_type = "grass"
                else:
                    block_type = "stone"
                block_color = self.block_colors[block_type]
                block_rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
                pygame.draw.rect(terrain, block_color, block_rect)
        return terrain

    def identify_forests(self, trees):
        forest_radius = 50
        for tree in trees:
            neighbors = [t for t in trees if ((t.x - tree.x)**2 + (t.y - tree.y)**2) <= forest_radius**2]
            if len(neighbors) >= 4:
                self.make_forest(tree.x, tree.y)

    def make_forest(self, x, y):
        forest_radius = 50
        for dx in range(-forest_radius, forest_radius):
            for dy in range(-forest_radius, forest_radius):
                if (dx**2 + dy**2) <= forest_radius**2:
                    try:
                        self.surface.set_at((x + dx, y + dy), self.block_colors["forest"])
                    except IndexError:
                        pass

import random

class Bush:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.berries = []
        self.month = 1
        self.month_duration_milliseconds = 5000  # 5 seconds per month

    def grow_berries(self):
        if 5 <= self.month <= 8:
            new_berry = (self.x + random.randint(-2, 2), self.y + random.randint(-2, 2))
            self.berries.append(new_berry)

    def remove_berry(self, index):
        del self.berries[index]

def update_bush_lifecycle(bushes):
    for bush in bushes:
        bush.month += 1
        if bush.month > 12:
            bush.month = 1
            bush.berries.clear()  # Remove all berries at the end of the year
        elif bush.month == 9:
            bush.berries.clear()  # Remove all berries in month 9

        bush.grow_berries()  # Grow berries during months 5 to 8

def generate_bushes(terrain_surface, biome_colors):
    bushes = []
    num_bushes = 50  # Adjust the number of bushes
    for _ in range(num_bushes):
        x = random.randint(0, terrain_surface.get_width() - 1)
        y = random.randint(0, terrain_surface.get_height() - 1)
        color_at_position = terrain_surface.get_at((x, y))[:3]  # Get RGB color
        if color_at_position in biome_colors.values() and color_at_position != biome_colors["water"] and color_at_position != biome_colors["sand"]:
            bushes.append(Bush(x, y))
    return bushes
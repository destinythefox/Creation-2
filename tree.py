import pygame
import random

class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0
        self.max_age = random.randint(50, 200)  # Adjust tree life span

def generate_trees(terrain_surface, biome_colors):
    trees = []
    
    num_trees = 300  # Increase the number of trees
    
    for _ in range(num_trees):
        x = random.randint(0, terrain_surface.get_width() - 1)
        y = random.randint(0, terrain_surface.get_height() - 1)
        
        color_at_position = terrain_surface.get_at((x, y))[:3]  # Get RGB color
        
        # Check if the position is suitable for a tree
        if color_at_position in biome_colors.values() and color_at_position != biome_colors["water"] and color_at_position != biome_colors["sand"]:
            trees.append(Tree(x, y))
            
    return trees

def update_tree_lifecycle(trees):
    for tree in trees:
        tree.age += 1
        if tree.age > tree.max_age:
            trees.remove(tree)  # Tree dies of old age

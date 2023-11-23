# nodes.py
import math

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

def create_and_connect_nodes(map_instance):
    grid_size_x, grid_size_y = map_instance.width, map_instance.height
    grid = [[None if not map_instance.map[i][j] else Node((i, j)) for j in range(grid_size_y)] for i in range(grid_size_x)]

    for i in range(grid_size_x):
        for j in range(grid_size_y):
            if grid[i][j] is not None:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < grid_size_x and 0 <= ny < grid_size_y and grid[nx][ny] is not None:
                            grid[i][j].add_neighbor(grid[nx][ny])

    # Aplatir la liste des nœuds tout en éliminant les valeurs None
    nodes = [node for row in grid for node in row if node is not None]
    return nodes


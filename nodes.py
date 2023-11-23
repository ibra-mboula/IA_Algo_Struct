import math
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)


def create_and_connect_nodes(num_nodes=50):
    grid_size = int(math.sqrt(num_nodes))
    grid = [[Node((i, j)) for j in range(grid_size)] for i in range(grid_size)]

    def connect_nodes(x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid_size and 0 <= ny < grid_size:
                    grid[x][y].add_neighbor(grid[nx][ny])

    for i in range(grid_size):
        for j in range(grid_size):
            connect_nodes(i, j)

    # Aplatir la liste des nœuds
    nodes = [node for row in grid for node in row]
    return nodes

# Vous pouvez appeler cette fonction dans votre main.py
nodes = create_and_connect_nodes()

# Après avoir créé les nœuds et établi leurs connexions
for node in nodes:
    print(f"Nœud {node.id}: voisins -> {[neighbor.id for neighbor in node.neighbors]}")

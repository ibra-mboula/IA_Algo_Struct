# nodes.py
import math

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        self.g = float('inf')  # Coût de déplacement jusqu'à ce nœud
        self.h = 0  # Heuristique (distance estimée jusqu'au nœud cible)
        self.f = float('inf')  # Coût total (g + h)
        self.parent = None  # Nœud parent
        

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

# A* algorithm

def heuristic(node, goal):
    # Utilisation de la distance euclidienne comme heuristique
    (x1, y1), (x2, y2) = node.id, goal.id
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def a_star(start, goal, map_instance):
    open_set = [start]
    start.g = 0
    start.f = heuristic(start, goal)
    

    while open_set:
        current = min(open_set, key=lambda o: o.f)
        print(f"Exploring Node: {current.id}, f: {current.f}")

        if current == goal:
            return reconstruct_path(current)

        open_set.remove(current)

        for neighbor in current.neighbors:
            tentative_g = current.g + 1  # Assumer un coût de déplacement constant
            if tentative_g < neighbor.g:
                neighbor.parent = current
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h

                if neighbor not in open_set:
                    open_set.append(neighbor)

    return None

def reconstruct_path(current):
    path = []
    while current:
        path.append(current.id)
        current = current.parent
    return path[::-1]  # Retourner le chemin inversé
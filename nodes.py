# nodes.py
import math

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        self.g = float('inf')  # Coût de déplacement jusqu'à ce nœud
        self.h = 0  # Heuristique (distance estimée jusqu'au nœud cible)
        self.f = float('inf')  # Coût total (g + h)
        self.parent = None  # Nœud parent => par défaut, aucun parent

        

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

def create_and_connect_nodes(map_instance):
    
    grid_size_x, grid_size_y = map_instance.width, map_instance.height
    grid = [[None if not map_instance.map[i][j] else Node((i, j)) for j in range(grid_size_y)] for i in range(grid_size_x)] #je créer une instance Node pour chaque coordonnées

    # ensuite, je lie les noeuds entre eux
    for i in range(grid_size_x):
        for j in range(grid_size_y):
            if grid[i][j] is not None:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0: # on vérifie cela pour éviter que le noeuds i,j  n'est pas son voisin
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
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) # formule a**2 = b**2 + c**2 et on cherche "a" qui est la distance

def a_star(start, goal, map_instance):
    open_set = [start]
    start.g = 0
    start.f = heuristic(start, goal)
    

    while open_set:
        current = min(open_set, key=lambda o: o.f) # on prend le noeud avec le coût total le plus petit car c'est le plus proche de noeud à atteindre
        #print(f"Exploring Node: {current.id}, f: {current.f}")

        # si le noeud courant est le noeud à atteindre alors on retourne le chemin
        if current.id == goal.id:
            return reconstruct_path(current)
        # sinon, on enlève le noeud courant
        open_set.remove(current)
        # et on ajoute les voisins de noeud current
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
        current = current.parent # on remonte le vrai chemin avec les parents de ce noeuds
    return path[::-1]  # Retourner le chemin inversé

def reset_nodes(nodes):
    for node in nodes:
        node.g = float('inf')
        node.h = 0
        node.f = float('inf')
        node.parent = None
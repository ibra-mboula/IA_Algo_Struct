import numpy as np

class Map:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.map = []
        self.position_door = []
        
        # Je commence à construire la map
        self.set_map()
    
    # create_matrix est la méthode qui va me retourner une matrice 2x2 selon la longueur et la hauteur
    def create_matrix(self):
        return np.zeros((self.height,self.width))
    
    # création de la map
    def set_map(self):
        matrix = self.create_matrix()
        
        # Avec cette matrice, je vais initialiser chaque position à true
        for i in range(self.width):
            for j in range(self.height):
                matrix[i,j] = True # True signifie que cette position est libre
        
        self.map = matrix
    
    # set_obstacles est la methode qui va initialiser les obstance en désactivant
    def set_obstacle(self,x,y,w,h): # matrix est considéré comme la map, une map est un ensemble de position en 2 dimensions
        # Un obstacles sera un rectangle à la position x,y avec un longueur de w et une hauteur de h
        # L'obstacle ne va que désactivé certains positions, car il y a un obstacle
        if(x <= self.width-1 and y <= self.height-1 and x+w <= self.width-1 and y+h <= self.height-1):
            for i in range(x,x+w):
                for j in range(y,y+h):
                    self.map[i,j] = False
        else:
            print("la dimension est mal dimensionné car elle dépasse la map")
            exit()
    
    # méthode qui va initialiser la position de la porte en repsectant que la porte soit dans la périphérie de la map
    def set_door_position(self, x, y):
        if x <= self.width-1 and y <= self.height-1:
            self.map[x,y] = 2 # on initialise le status à 2
            self.position_door = [x,y]
        else:
            print(f"la position de la porte est mauvaise, la taille de la matrice est [{self.width},{self.height}]")
            exit()
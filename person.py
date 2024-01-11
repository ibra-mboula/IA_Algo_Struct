class person:
    def __init__(self, map, position, speed) -> None:
        self.map = map # environnement selon la perspective de la personne car pour lui, les autrs sont des obstacles
        self.position = position # position de la personne
        self.speed = speed # vitesse de la personne (point/déplacement)

    def make_new_map(self,all_obstacle): # créer la nouvelle map mais par rapport à la perception de cette personne
        pass
import nodes as nd
from plot import plot_map_with_nodes


class person:
    def __init__(self, map, position, speed, nodes_cpy = []) -> None:
        self.map = map # environnement selon la perspective de la personne car pour lui, les autrs sont des obstacles
        self.position = position # position de la personne
        self.speed = speed # vitesse de la personne (point/déplacement)
        self.nodes_cpy = nodes_cpy
        self.arrived = False
        self.each_movement = [] # chaque item de la table correspond à un mouvement d'une personne

    def make_new_map(self,other_peoples, map_without_person): # créer la nouvelle map mais par rapport à la perception de cette personne
        # je modifie d'abord le clone de la map sans personne
        for other_person in other_peoples:
            map_without_person.set_obstacle(x=other_person.position[0], y=other_person.position[1])
        # Et enfin, je peux remplacer la perception de la map de la personne
        self.map = map_without_person

    def make_movement(self,goal_node): # cette fonction va être appelé pour chaque personne pour qu'elle
            # je vérifie que la personne n'est pas déjà arrivé
            if goal_node.id == self.position:
                 self.arrived = True 

            if not self.arrived:
                start_node = next(node for node in self.nodes_cpy if node.id == (self.position[0], self.position[1])) # je récupère le noeud de départ

                # Réinitialiser les nœuds avant chaque parcours
                nd.reset_nodes(self.nodes_cpy)

                # Appel de l'algorithme A* pour le parcours
                path = nd.a_star(start_node, goal_node, self.map)
                #print(f"Chemin trouvé: {path}")

                # pour vérifier que les autres personnes sont des obstacles
                #plot_map_with_nodes(self.map, self.nodes_cpy, [path])

                return path
            else:
                return None

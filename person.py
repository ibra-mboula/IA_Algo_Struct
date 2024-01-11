import nodes as nd
from plot import plot_map_with_nodes


class person:
    def __init__(self, map, position, speed, nodes_cpy = []) -> None:
        self.map = map # environnement selon la perspective de la personne car pour lui, les autrs sont des obstacles
        self.position = position # position de la personne
        self.speed = speed # vitesse de la personne (point/déplacement)
        self.nodes_cpy = nodes_cpy

    def make_new_map(self,other_peoples): # créer la nouvelle map mais par rapport à la perception de cette personne
        for other_person in other_peoples:
            self.map.set_obstacle(x=other_person.position[0], y=other_person.position[1])

    def make_movement(self,goal_node): # cette fonction va être appelé pour chaque personne pour qu'elle
            paths = []
            start_node = next(node for node in self.nodes_cpy if node.id == (self.position[0], self.position[1])) # je récupère le noeud de départ

            # Réinitialiser les nœuds avant chaque parcours
            nd.reset_nodes(self.nodes_cpy)

            # Appel de l'algorithme A* pour le parcours
            path = nd.a_star(start_node, goal_node, self.map)
            print(f"Chemin trouvé: {path}")
            paths.append(path)

            # pour vérifier que les autres personnes sont des obstacles
            plot_map_with_nodes(self.map, self.nodes_cpy, paths)

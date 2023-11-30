# main.py
import init_map as im
import nodes as nd
from plot import plot_map_with_nodes  

def main():
    # Initialisation de la carte avec des obstacles et une porte
    mp = im.Map(10, 10)
    mp.set_obstacle(x=1, y=1, w=3, h=3)
    mp.set_obstacle(x=5, y=5, w=1, h=1)
    
    #mp.set_door_position(9, 6)

    # Création et connexion des nœuds selon la carte
    all_nodes = nd.create_and_connect_nodes(mp)

    # Saisie utilisateur pour le nœud de sortie
    goal_x, goal_y = map(int, input("Entrez les coordonnées du nœud de sortie (x y): ").split())
    goal_node = next(node for node in all_nodes if node.id == (goal_x, goal_y))

    paths = []
    while True:
        # Saisie utilisateur pour les nœuds de départ
        start_input = input("Entrez les coordonnées d'un nœud de départ (x y) ou 'fin' pour terminer: ")
        if start_input.lower() == 'fin':
            break

        start_x, start_y = map(int, start_input.split())
        start_node = next(node for node in all_nodes if node.id == (start_x, start_y))

        # Réinitialiser les nœuds avant chaque parcours
        nd.reset_nodes(all_nodes)

        # Appel de l'algorithme A* pour le parcours
        path = nd.a_star(start_node, goal_node, mp)
        print(f"Chemin trouvé: {path}")
        paths.append(path)

    # Affichage des nœuds et de la map avec les chemins
    plot_map_with_nodes(mp, all_nodes, paths)

if __name__ == "__main__":
    main()

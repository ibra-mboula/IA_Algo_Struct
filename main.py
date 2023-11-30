# main.py
import init_map as im
import nodes as nd
from plot import plot_map_with_nodes  

def main():
    # Initialisation de la carte avec des obstacles et une porte
    mp = im.Map(10, 10)
    mp.set_obstacle(x=1, y=1, w=3, h=3)
    mp.set_obstacle(x=5, y=5, w=1, h=1)
    
    mp.set_door_position(9, 6)

    # Création et connexion des nœuds selon la carte
    all_nodes = nd.create_and_connect_nodes(mp)
    
    # Définir les points de départ et d'arrivée pour deux parcours
    start_node_1 = next(node for node in all_nodes if node.id == (0, 0))
    goal_node_1 = next(node for node in all_nodes if node.id == (6, 9))
    
    # Réinitialiser les nœuds pour le second parcours
    nd.reset_nodes(all_nodes)
    
    start_node_2 = next(node for node in all_nodes if node.id == (5, 0))
    goal_node_2 = next(node for node in all_nodes if node.id == (6, 9))

# Premier parcours A*
    path_1 = nd.a_star(start_node_1, goal_node_1, mp)
    print("Chemin 1 trouvé:", path_1)

    # Réinitialiser les nœuds pour le second parcours
    nd.reset_nodes(all_nodes)

    # Définir les points de départ et d'arrivée pour le second parcours
    start_node_2 = next(node for node in all_nodes if node.id == (1, 4))
    goal_node_2 = next(node for node in all_nodes if node.id == (6, 9))

    # Second parcours A*
    path_2 = nd.a_star(start_node_2, goal_node_2, mp)
    print("Chemin 2 trouvé:", path_2)

    # Affichage des nœuds et de la map avec les chemins
    plot_map_with_nodes(mp, all_nodes, [path_1, path_2])

if __name__ == "__main__":
    main()

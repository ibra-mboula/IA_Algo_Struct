# main.py
import init_map as im
import nodes as nd
from plot import plot_map_with_nodes  

def main():
    # Initialisation de la carte avec des obstacles et une porte
    mp = im.Map(10, 10)
    mp.set_obstacle(x=1, y=1, w=3, h=3)
    mp.set_obstacle(x=5, y=5, w=1, h=1)
    
    mp.set_door_position(9, 0)

    # Création et connexion des nœuds selon la carte
    nodes = nd.create_and_connect_nodes(mp)

    # Affichage des nœuds et de la map
    plot_map_with_nodes(mp, nodes)

    # Impression des détails des nœuds pour vérifier
    for node in nodes:
        print(f"Nœud {node.id}: voisins -> {[neighbor.id for neighbor in node.neighbors]}")


if __name__ == "__main__":
    main()

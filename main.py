# main.py
import init_map as im
import nodes as nd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def plot_map_with_nodes(map_instance, nodes):
    fig, ax = plt.subplots()
    # Tracer les obstacles
    for i in range(map_instance.width):
        for j in range(map_instance.height):
            if not map_instance.map[i][j]:  # Si c'est un obstacle
                ax.plot(i, j, 's', color='red')  # Dessiner un carré rouge



    # Tracer les nœuds et leurs connexions
    for node in nodes:
        x, y = node.id
        ax.plot(x, y, 'o', color='blue')  # Dessiner le nœud
        
        # Tracer la position de la porte en jaune
        door_x, door_y = map_instance.position_door
        ax.plot(door_x, door_y, 's', color='yellow')  # Dessiner un carré jaune
        
        
        
        for neighbor in node.neighbors:
            nx, ny = neighbor.id
            line = mlines.Line2D([x, nx], [y, ny], color='gray')
            ax.add_line(line)

    ax.set_xlim(-1, map_instance.width)
    ax.set_ylim(-1, map_instance.height)
    

    
    plt.show()

def main():
    # Initialisation de la carte avec des obstacles et une porte
    mp = im.Map(10, 10)
    mp.set_obstacle(x=1, y=1, w=2, h=3)
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

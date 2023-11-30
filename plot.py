import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def plot_map_with_nodes(map_instance, nodes, paths=None):
    fig, ax = plt.subplots()

    # Tracer les obstacles
    for i in range(map_instance.width):
        for j in range(map_instance.height):
            if not map_instance.map[i][j]:  # Si c'est un obstacle
                ax.plot(i, j, 's', color='red')  # Dessiner un carré rouge

    # Tracer la position de la porte en jaune
    door_x, door_y = map_instance.position_door
    ax.plot(door_x, door_y, 's', color='yellow')  # Dessiner un carré jaune

    # Tracer les nœuds et leurs connexions
    for node in nodes:
        x, y = node.id
        ax.plot(x, y, 'o', color='blue')  # Dessiner le nœud
        for neighbor in node.neighbors:
            nx, ny = neighbor.id
            line = mlines.Line2D([x, nx], [y, ny], color='gray', linewidth=0.5)
            ax.add_line(line)

    # Tracer les chemins si fournis
    if paths:
        for path in paths:
            if path is not None:  # Ajoutez cette vérification
                for i in range(len(path) - 1):
                    start = path[i]
                    end = path[i + 1]
                    line = mlines.Line2D([start[0], end[0]], [start[1], end[1]], color='green')
                    ax.add_line(line)

    ax.set_xlim(-1, map_instance.width)
    ax.set_ylim(-1, map_instance.height)
    plt.show()

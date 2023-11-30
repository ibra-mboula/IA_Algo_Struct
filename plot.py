import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_map_with_nodes(map_instance, nodes, paths):
    fig, ax = plt.subplots()

    # Dessiner la grille
    for x in range(map_instance.width):
        for y in range(map_instance.height):
            if not map_instance.map[x][y]:
                ax.add_patch(patches.Rectangle((y, x), 1, 1, color='black'))

    # Dessiner la porte
    if map_instance.position_door:
        door_x, door_y = map_instance.position_door
        ax.add_patch(patches.Rectangle((door_y, door_x), 1, 1, color='green'))

    # Dessiner les nœuds et leurs connexions
    for node in nodes:
        x, y = node.id
        ax.plot(y + 0.5, x + 0.5, marker='o', color='red', markersize=5)
        for neighbor in node.neighbors:
            nx, ny = neighbor.id
            ax.plot([y + 0.5, ny + 0.5], [x + 0.5, nx + 0.5], color='gray', linestyle='--')

    # Dessiner les chemins
    for path in paths:
        if path:
            for i in range(len(path) - 1):
                start = path[i]
                end = path[i + 1]
                ax.plot([start[1] + 0.5, end[1] + 0.5], [start[0] + 0.5, end[0] + 0.5], color='blue', linewidth=2)

    # Configurer les axes
    ax.set_xlim(0, map_instance.width)
    ax.set_ylim(0, map_instance.height)
    ax.set_xticks(range(map_instance.width))
    ax.set_yticks(range(map_instance.height))
    ax.grid(which='both')
    ax.set_aspect('equal', adjustable='box')

    plt.show()

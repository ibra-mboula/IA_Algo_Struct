# main.py
import init_map as im
import nodes as nd
from plot import plot_map_with_nodes
from person import person as ps

def set_obstacle_in_map(map,position_obstacle):
    for item in position_obstacle:
        if "w" in item: # ca signifie que la largeur et la hauteur est spécifié
            map.set_obstacle(x=item["x"], y=item["y"], w=item["w"], h=item["h"])
        else:
            map.set_obstacle(x=item["x"], y=item["y"])
            
    return map

# dimenson de la map
map_width = 20
map_height = 20

# placement des obstacles
obstacles=[ {"x":1,"y":1,"w":3,"h":3} , {"x":5,"y":5}] # obstacle par défaut de l'environnement (des tables, des chaises etc)

# Initialisation de la carte avec des obstacles et une porte
mp = im.Map(map_width, map_height)
set_obstacle_in_map(mp,obstacles)
#mp.set_obstacle(x=1, y=1, w=3, h=3)
#mp.set_obstacle(x=5, y=5)


def main():
    
    # Création et connexion des nœuds selon la carte
    all_nodes = nd.create_and_connect_nodes(mp)

    # Saisie utilisateur pour le nœud de sortie
    goal_x, goal_y = map(int, input("Entrez les coordonnées du nœud de sortie (x y): ").split())
    try:
        goal_node = next(node for node in all_nodes if node.id == (goal_x, goal_y))
    except:
        print("mauvaise coordonnées de la porte de sortie !!")
        exit()

    position_people = [{"x":0, "y":0,"v":3},{"x":8, "y":9,"v":1}]  # tableau qui contient les positions de chaque personne dans la pièce
    # x et y correspond à la position de la personne et v est sa vitesse

    # je commence par créer les instance de personnes
    peoples = []
    for item in position_people:
        peoples.append(ps(map=mp, position=(item["x"],item["y"]),speed=item["v"]))

    paths = []
    while True:
        # Saisie utilisateur pour les nœuds de départ
        start_input = input("Entrez les coordonnées d'un nœud de départ (x y) ou 'fin' pour terminer: ")
        if start_input.lower() == 'fin':
            break

        start_x, start_y = map(int, start_input.split())
        start_node = next(node for node in all_nodes if node.id == (start_x, start_y)) # je récupère le noeud de départ

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

# main.py
import math
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

def update_map_for_each_person(peoples):
    for person in peoples:
        peoples_array_cloned = peoples.copy()  # Je fais une copie du tableau de personnes en enlevant bien sûr la personne du tableau
        peoples_without_person = [p for p in peoples_array_cloned if p != person]
        person.make_new_map(other_peoples=peoples_without_person)
        person.nodes_cpy = nd.create_and_connect_nodes(person.map)

def distance(position1, position2):
    return math.sqrt((position2[0] - position1[0])**2 + (position2[1] - position1[1])**2)

def person_sorted_by_distance(peoples, position_objectif):

    positions_peoples = []
    for person in peoples:
        positions_peoples.append(person.position)

    # triée le tableau selon la distance entre la position de la personne et la position du goal
    positions_sorted = sorted(positions_peoples, key=lambda pos: distance(pos, position_objectif))

    # maintenant je dois retrouver l'instance de la personne
    peoples_sorted = []
    for position in positions_sorted:
        for person in peoples:
            if person.position == position:
                peoples_sorted.append(person)

    return peoples_sorted


# dimenson de la map
map_width = 20
map_height = 20

# placement des obstacles
obstacles=[ {"x":1,"y":1,"w":3,"h":3} , {"x":5,"y":5}] # obstacle par défaut de l'environnement (des tables, des chaises etc)


def main():

    # Initialisation de la carte avec des obstacles et une porte
    mp = im.Map(map_width, map_height)
    set_obstacle_in_map(mp,obstacles)
    #mp.set_obstacle(x=1, y=1, w=3, h=3)
    #mp.set_obstacle(x=5, y=5)

    # Création et connexion des nœuds selon la carte
    all_nodes = nd.create_and_connect_nodes(mp)

    # Saisie utilisateur pour le nœud de sortie
    goal_x, goal_y = map(int, input("Entrez les coordonnées du nœud de sortie (x y): ").split())
    try:
        goal_node = next(node for node in all_nodes if node.id == (goal_x, goal_y))
    except:
        print("mauvaise coordonnées de la porte de sortie !!")
        exit()

    position_people = [{"x":0, "y":0,"v":3},{"x":8, "y":9,"v":1},{"x":0, "y":3,"v":6}]  # tableau qui contient les positions de chaque personne dans la pièce
    # x et y correspond à la position de la personne et v est sa vitesse

    # je commence par créer les instance de chaque personne
    peoples = []
    for person in position_people:
        peoples.append(ps(map=mp.__copy__(), position=(person["x"],person["y"]),speed=person["v"], nodes_cpy=all_nodes.copy()))# petit point -> je fait une copie de la map et noeud par défaut pour chaque individue

    # ensuite, je vai(s changer l'environnement selon la perception des personnes => une personne est une obstacles pour la personne qui va bouger
    update_map_for_each_person(peoples=peoples)

    # Maintenant que les autres personnes sont considéré comme des obstacles, je peux alors commencer à faire bouger une personne par une

    # avant de faire ca, je dois trouvé le personne la plus proche du goal -> enfaite les triers
    people_sorted = person_sorted_by_distance(peoples=peoples, position_objectif=goal_node.id)

    for person in people_sorted:
        person.make_movement(goal_node)

if __name__ == "__main__":
    main()

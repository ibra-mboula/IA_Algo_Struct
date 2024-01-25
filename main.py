# main.py
import math
import init_map as im
import nodes as nd
from plot import plot_map_with_nodes
from person import person as ps
from animat import animate
import copy
import random

def set_obstacle_in_map(map,position_obstacle):
    for item in position_obstacle:
        if "w" in item: # ca signifie que la largeur et la hauteur est spécifié
            map.set_obstacle(x=item["x"], y=item["y"], w=item["w"], h=item["h"])
        else:
            map.set_obstacle(x=item["x"], y=item["y"])
            
    return map

def update_map_for_each_person(peoples, original_map_without_peoples):
    for person in peoples:
        peoples_array_cloned = peoples.copy()  # Je fais une copie du tableau de personnes en enlevant bien sûr la personne du tableau
        peoples_without_person = [p for p in peoples_array_cloned if p != person]
        person.make_new_map(other_peoples=peoples_without_person, map_without_person=original_map_without_peoples.__copy__())
        person.nodes_cpy = nd.create_and_connect_nodes(person.map)
    return peoples

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
map_width = 62
map_height = 30

# placement des obstacles
obstacles=[ {"x":1,"y":1,"w":3,"h":3} , {"x":5,"y":5}, {"x":20,"y":16,"w":10,"h":3},{"x":40,"y":10,"w":10,"h":15},{"x":32,"y":6,"w":3,"h":18}] # obstacle par défaut de l'environnement (des tables, des chaises etc)
position_people = [{"x":0, "y":0,"v":10},{"x":8, "y":19,"v":1},{"x":9, "y":19,"v":1},{"x":10, "y":19,"v":2}]  # tableau qui contient les positions de chaque personne dans la pièce

def main():

    # Initialisation de la carte avec des obstacles et une porte
    mp = im.Map(map_width, map_height)
    set_obstacle_in_map(mp,obstacles)
    #mp.set_obstacle(x=1, y=1, w=3, h=3)
    #mp.set_obstacle(x=5, y=5)

    # Création et connexion des nœuds selon la carte
    all_nodes = nd.create_and_connect_nodes(mp)

    # Saisie utilisateur pour le nœud de sortie
    #goal_x, goal_y = map(int, input("Entrez les coordonnées du nœud de sortie (x y): ").split()) # ===> à décommenter
    goal_x = 61
    goal_y = 29
    try:
        goal_node = next(node for node in all_nodes if node.id == (goal_x, goal_y))
    except:
        print("mauvaise coordonnées de la porte de sortie !!")
        exit()

    # x et y correspond à la position de la personne et v est sa vitesse

    # je commence par créer les instance de chaque personne
    peoples = []
    for person in position_people:
        peoples.append(ps(map=mp.__copy__(), position=(person["x"],person["y"]),speed=person["v"], nodes_cpy=all_nodes.copy()))# petit point -> je fait une copie de la map et noeud par défaut pour chaque individue


    # boucle par mouvement
    # je vérifie s'il manque des personnes
    arrived = []
    for person in peoples:
        arrived.append(person.arrived)

    # et je créer un tableau avec les personnes qui sont sortie de la map
    people_who_go_out = []

    while False in arrived:
        # ensuite, je vais changer l'environnement selon la perception des personnes => une personne est une obstacles pour la personne qui va bouger
        peoples = update_map_for_each_person(peoples=peoples, original_map_without_peoples=mp)

        # Maintenant que les autres personnes sont considéré comme des obstacles, je peux alors commencer à faire bouger une personne par une

        # avant de faire ca, je dois trouvé le personne la plus proche du goal -> enfaite les triers
        people_sorted = person_sorted_by_distance(peoples=peoples, position_objectif=goal_node.id)

        # et la je commence les mouvements selon le trie
        paths_per_person = {}
        for person in people_sorted:
            best_path = person.make_movement(goal_node)
            if best_path is not None:
                paths_per_person[person] = best_path
            else:
                paths_per_person[person] = [] # La personne est arrivée, le tableau doit alors être vide
        # et maintenant, je peut couper le chemin parfait selon la vitesse de la personne
        for path in paths_per_person:
            best_way_per_step = [ ]
            if len(paths_per_person[path])-1 > path.speed:
                # je prend alors la partie qu'il faut
                for i in range(path.speed+1):
                    best_way_per_step.append(paths_per_person[path][i])
                #print(best_way_per_step)
                path.each_movement.append(best_way_per_step) # je save le mouvement
                path.position = best_way_per_step[len(best_way_per_step)-1]
            else:
                # ca signifie que le goal a été atteint donc la personne n'est plus un obstacle donc je dois juste l'enlever des peoples
                path.arrived =True
                best_way_per_step = paths_per_person[path]
                if len(best_way_per_step) != 0:
                    path.position = best_way_per_step[len(best_way_per_step)-1]
                    #print(best_way_per_step)
                    path.each_movement.append(best_way_per_step) # je save le mouvement
                else:
                    pass
                    #print("la personne est déjà sortie")
        #print("\n")

        # j'efface les personne qui sont sortie
        people_who_do_not_goOut = {}
        for person in paths_per_person:
            if not person.arrived:# s'il n'est pas arrivé je met la personne dans le tableau des personne qui sont pas sortie
                people_who_do_not_goOut[person] = paths_per_person[person]
            else:# sinon, si la personne est sortie alors je save dans le tableau des personne qui sont sortie
                people_who_go_out.append(person)

        # et à la fin, j'utilise les instances de person et je l'ai met dans people ET je recalcule si toutes les personnes sont arrivées
        peoples.clear()
        for person in people_who_do_not_goOut:
            peoples.append(person)

        arrived.clear()
        for person in peoples:
            arrived.append(person.arrived)
        
    return mp,goal_node.id,people_who_go_out


if __name__ == "__main__":
    map,goal_node_id,step_per_person = main()
    ani = animate(map=map, goal_node_id=goal_node_id, step_people=step_per_person)
    ani.launch_animation()

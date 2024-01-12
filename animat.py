import pygame
import numpy as np

class animate:
    def __init__(self, map, goal_node_id, step_people) -> None:
        self.map = map
        self.data = step_people
        # j'initialise la position goal en 2 pour qu'il soit dessiner en vert
        self.map.map[goal_node_id[0], goal_node_id[1]] = 2

    def launch_animation(self):
        # Initialisation de Pygame
        pygame.init()

        # Paramètres de la fenêtre et de la taille des case pour les obstacles, porte de sortie etc
        largeur_fenetre = 800
        hauteur_fenetre = 800
        taille_case = 16 # pour que les bord soit bon => 16.49=784 envirion 800 pixels c'est bon

        # Création de la fenêtre avec un titre
        fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
        pygame.display.set_caption("Ma Carte Pygame")

        # matrice qui va contenir les informations de la map
        matrice = self.map.map

        # Couleurs
        couleur_case_vide = (255, 255, 255) # blanc si y a rien
        couleur_case_pleine = (96,96,96) # gris s'il y a des obstacles
        couleur_sortie = (0,86,27) # couleur vert pour la sortie 

        # Boucle principale
        running = True
        iterator_mouvement = 0 # me permet de savoir à quelle mouvement sont les personnes
        movement = self.next_move(iterator=iterator_mouvement) # tableau qui va contenir le mouvement pour chaque personne

        step_movement = 0 # permet de savoir à quelle  étapes est le mouvement

        while running:
            # je récupére tous type d'event et si l'event et que l'utilisateur ferme la fenêtre alors pygame s'arrète
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Effacer tous ce qu'il y a dans l'écran
            fenetre.fill((255, 255, 255))

            # Afficher la matrice des obstacles ainsi que de la porte de sortie
            for i in range(matrice.shape[0]):
                for j in range(matrice.shape[1]):
                    x = j * taille_case
                    y = i * taille_case
                    if matrice[i, j] == 1: # si la valeur de cette coordonné est 1, ca signifiait True donc la case est vide
                        pygame.draw.rect(fenetre, couleur_case_vide, (x, y, taille_case, taille_case))
                    elif matrice[i,j] == 0: # sinon, si c'est null ca signifie qu'il y a une obstacle donc je dessine en gris
                        pygame.draw.rect(fenetre, couleur_case_pleine, (x, y, taille_case, taille_case))
                    elif matrice[i,j] == 2: # et si c'est 2 alors on est à la sortie
                        pygame.draw.rect(fenetre, couleur_sortie, (x, y, taille_case, taille_case))

            # Afficher la position des personnes et actualiser leur position
            for move in movement:
                pygame.draw.rect(fenetre, (0,0,0), (move[0][0][0]* taille_case, move[0][0][1]* taille_case, taille_case, taille_case))


            # Mettre à jour l'affichage
            pygame.display.flip()

        # Quitter Pygame
        pygame.quit()
    
    def next_move(self, iterator) -> list:
        
        array_to_return = [] # contient les positions de chaque personne qui sont dans la pièces
        for person in self.data:
            if len(person.each_movement) > iterator: # tant qu'on dépasse le nombre de mouvement de la personne c'est je prend son mouvement
                array_to_return.append([person.each_movement[iterator]])
        
        return array_to_return



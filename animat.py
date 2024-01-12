import pygame
import numpy as np

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600
taille_case = 20

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Ma Carte Pygame")

# Votre matrice NumPy
matrice = np.array([[1, 0, 1, 0, 1],
                    [0, 1, 0, 1, 0],
                    [1, 0, 1, 0, 1],
                    [0, 1, 0, 1, 0]])

# Couleurs
couleur_case_vide = (255, 255, 255)
couleur_case_pleine = (0, 0, 0)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer l'écran
    fenetre.fill((255, 255, 255))

    # Afficher la matrice
    for i in range(matrice.shape[0]):
        for j in range(matrice.shape[1]):
            x = j * taille_case
            y = i * taille_case
            if matrice[i, j] == 1:
                pygame.draw.rect(fenetre, couleur_case_pleine, (x, y, taille_case, taille_case))
            else:
                pygame.draw.rect(fenetre, couleur_case_vide, (x, y, taille_case, taille_case))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()

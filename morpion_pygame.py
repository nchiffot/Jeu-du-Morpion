import pygame, sys
import numpy as np

pygame.init()

LARGEUR_ECRAN = 600
HAUTEUR_ECRAN = 600
LARGEUR_LIGNE = 15
TABLEAU_ROW = 3
TABLEAU_COL = 3
CERCLE_RAYON =60
CERCLE_LARGEUR = 15
CERCLE_COULEUR = (239, 231, 200)
CROIX_LARGEUR  = 25
SPACE = 55
CROIX_COULEUR = (66, 66, 66)


RED = (255, 0, 0)
FOND_ECRAN = (28, 170, 156)
COULEUR_LIGNE =(155, 155 ,155)
couleur = (0,0,0)

# affiche l'écran
ecran = pygame.display.set_mode((LARGEUR_ECRAN,HAUTEUR_ECRAN))
pygame.display.set_caption('morpion')
ecran.fill(FOND_ECRAN)

# Tableau qui indique l'avancement du jeu
Tableau = np.zeros((TABLEAU_ROW,TABLEAU_COL))
# print(Tableau)

# Fonction qui génère la grille
def genere_ligne():
    #horizontal
    pygame.draw.line(ecran, COULEUR_LIGNE, (0, 200), (600, 200), LARGEUR_LIGNE)
    pygame.draw.line(ecran, COULEUR_LIGNE, (0, 400), (600, 400), LARGEUR_LIGNE)
    # vertical
    pygame.draw.line(ecran, COULEUR_LIGNE, (200, 0), (200, 600), LARGEUR_LIGNE)
    pygame.draw.line(ecran, COULEUR_LIGNE, (400, 0), (400, 600), LARGEUR_LIGNE)

# fonction qui dessine la croix ou le rond
def genere_motif():
    for row in range(TABLEAU_ROW):
        for col in range(TABLEAU_COL):
            if Tableau[row][col] == 1:
                pygame.draw.circle(ecran, CERCLE_COULEUR, (int(col*200 + 100), int(row*200 + 100)), CERCLE_RAYON, CERCLE_LARGEUR)
            elif Tableau[row][col] == 2:
                pygame.draw.line(ecran, CROIX_COULEUR, (col*200+SPACE, row*200+200-SPACE),(col*200 +200-SPACE, row*200+SPACE), CROIX_LARGEUR)
                pygame.draw.line(ecran, CROIX_COULEUR, (col* 200 + SPACE, row* 200 + SPACE),(col * 200 + 200 - SPACE, row * 200 +200- SPACE),CROIX_LARGEUR)

#fonction qui place le joueur
def placement(row, col, joueur):
    Tableau[row][col] = joueur

'''placement(0,0,1)
placement(1,2,2)
print(Tableau)'''

#fonction qui vérifie que la place est vide donc dispo
def placement_disponible(row,col):
    return Tableau[row][col] == 0
'''print(placement_disponible(1,2))
print(placement_disponible(0,1))'''

# fonction vérifie si le tableau est rempli ou non
def is_tableau_plein():
    for row in range(TABLEAU_ROW):
        for col in range(TABLEAU_COL):
            if Tableau[row][col] == 0:
                print("touche R pour redémarrer")
                return False
    return True
# fonction qui vérifie s'il y a un gagnant
def gagnant(joueur):
    #vertical
    for col in range(TABLEAU_COL):
        if Tableau[0][col] == Tableau[1][col] == Tableau[2][col] == joueur:
            print(joueur, 'gagne!')
            gagnant_vertical(col, joueur)
            return True
    #horizontal
    for row in range(TABLEAU_ROW):
        if Tableau[row][0] == Tableau[row][1] == Tableau[row][2] == joueur:
            print(joueur, 'gagne!')
            gagnant_horizontal(row, joueur)
            return True

    # diagonale montante
    if Tableau[2][0] == Tableau[1][1] == Tableau[0][2] ==joueur:
        print(joueur,'gagne!')
        gagnant_diagonale_up(joueur)
        return True
    # diagonale descendante
    if Tableau[0][0] == Tableau[1][1] == Tableau[2][2] ==joueur:
        print(joueur, 'gagne!')
        gagnant_diagonale_down(joueur)
        return True

    return False

def gagnant_vertical(col, joueur):
    couleur = CERCLE_COULEUR
    if joueur == 1:
        couleur = CERCLE_COULEUR
    elif joueur == 2:
        couleur = CROIX_COULEUR
    pygame.draw.line(ecran, couleur, (col*200+100, 15), (col*200+100, 585), 15 )

def gagnant_horizontal(row, joueur):
    couleur = CERCLE_COULEUR
    if joueur == 1:
        couleur = CERCLE_COULEUR
    elif joueur == 2:
        couleur = CROIX_COULEUR
    pygame.draw.line(ecran, couleur, (15, row * 200 +100), (585, row * 200 + 100), 15)

def gagnant_diagonale_up(joueur):
    couleur = CERCLE_COULEUR
    if joueur == 1:
        couleur = CERCLE_COULEUR
    elif joueur == 2:
        couleur = CROIX_COULEUR
    pygame.draw.line(ecran, couleur, (15, 585), (585, 15), 15)

def gagnant_diagonale_down(joueur):
    couleur = CERCLE_COULEUR
    if joueur == 1:
        couleur = CERCLE_COULEUR
    elif joueur == 2:
        couleur = CROIX_COULEUR



def restart():
    ecran.fill(FOND_ECRAN)
    genere_ligne()
    print(joueur, game_over)
    for row in range(TABLEAU_ROW):
        for col in range(TABLEAU_COL):
            Tableau[row][col]=0
    print(Tableau)

'''for row in range(TABLEAU_ROW):
    for col in range(TABLEAU_COL):
        placement(row, col, 1)
print(Tableau)
print(is_tableau_plein())'''

genere_ligne()
joueur = 1
game_over = False


# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] # abscisse de la position de la souris
            mouseY = event.pos[1] # ordonnée de la position de la souris
            #print(mouseX,mouseY)
            clicked_row = int(mouseX//200)
            clicked_col = int(mouseY//200)
            #print(clicked_row,clicked_col)

            if placement_disponible(clicked_col,clicked_row):
                if joueur == 1:
                    placement(clicked_col, clicked_row, 1)
                    if gagnant(joueur):
                        print("touche R pour redémarer")
                        game_over =True
                    joueur = 2
                elif joueur == 2:
                    placement(clicked_col, clicked_row, 2)
                    if gagnant(joueur):
                        print("touche R pour redémarer")
                        game_over = True
                    joueur = 1
                #print(Tableau)
                genere_motif()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                joueur = 1
                game_over = False






    pygame.display.update()

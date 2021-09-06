#!/usr/bin/python3
'''
Nous avons conçu un jeu appelé ANGAL,
qui permet à un personnage de se déplacer
dans un donjon entre des salles. Le but du
jeu est de récupérer des élixirs magiques.
'''

from random import randint, choice
import os
import curses
from point import Point
from salle import Salle
from personnage import Personnage



def placer_eau(categorie, salle, L):
    """
    Méthode qui permet de placer les
    sept eaux magiques dans les salles du jeu.
    """
    n = randint(salle.x, salle.x + salle.largeur)
    m = randint(salle.y, salle.y + salle.hauteur)
    L[m][n] = categorie
    return L


def ecrire_fichier(plateforme):
    """
    Méthode qui permet de stocker le jeu
    après chaque déplacement dans un fichier jeu.txt
    """
    fichier = open("jeu.txt", 'w')
    for i in range(len(plateforme)):
        for j in range(len(plateforme[0])):
            fichier.write(plateforme[i][j])
        fichier.write('\n')
    fichier.close()


def afficher_sous_fenetre(window):
    """
    Méthode qui permet d'afficher le contenu du fichier
    jeu.txt dans une console.
    """
    fichier = open('jeu.txt', 'r')
    n_ligne = 0
    for ligne in fichier.readlines():
        window.addstr(n_ligne + 1, 1, ligne[:50])
        n_ligne += 1
    fichier.close()


def main():
    """
    Programme principal du jeu
    """

# Création d'une plateforme vierge

    plateforme = [['I' for _ in range(50)]for _ in range(25)]
    eaux = ['R', 'B', 'Y', 'W', 'G', 'M', 'B']

# Initialisation du jeu

    print('Welcome to ANGAL WORLD!')
    level = int(input('Please enter a level : '))

# Création des salles + salle enter + salle quit

    liste_salles = []
    enter = Salle(1, 1, 2, 1)
    enter.afficher_salle(plateforme)
    liste_salles.append(enter)
    for _ in range(level):
        x, y = randint(0, 38), randint(0, 18)
        salle = Salle(x, y, 10, 5)
        liste_salles.append(salle)
        salle.afficher_salle(plateforme)
    quit = Salle(46, 22, 2, 1)
    quit.afficher_salle(plateforme)
    liste_salles.append(quit)

# Liaison des salles par des couloirs

    for i in range(level + 1):
        liste_salles[i].liaison_couloir(liste_salles[i+1], plateforme)

# Placer les Eaux Magiques

    j = 0
    while j < 7:
        placer_eau(eaux[j], liste_salles[j + 1], plateforme)
        j += 1

# Personnage

    personnage = Personnage()
    personnage.afficher_personnage(liste_salles[0], plateforme)
    ecrire_fichier(plateforme)

# Travail sous console

    curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    window = curses.newwin(27, 52, 1, 1)
    window.border(0)
    window.keypad(1)
    afficher_sous_fenetre(window)
    choix = window.getch()

# Gestion du déplacement du Personnage

    while 1:
        personnage.deplacement(choix, plateforme)
        ecrire_fichier(plateforme)
        afficher_sous_fenetre(window)
        choix = window.getch()

main()

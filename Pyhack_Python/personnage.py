#!/usr/bin/python3
"""
Après avoir tracer la plateforme, les salles et les couloirs
nous allons manipuler le personnage, son affichage et son déplacement
"""
from point import Point
from salle import Salle
import os
import curses


class Personnage(Point):
    def __init__(self):
        self.pers = '@'

    def afficher_personnage(self, salle, plateforme):
        '''
        Afficher le caractère @ dans la liste
        qui représentera le personnage.
        '''
        plateforme[salle.y][salle.x] = self.pers
        self.x = salle.x
        self.y = salle.y
        return plateforme

    def verification_deplacement(self, p, L):
        '''
        Méthode qui assure l'existence d'une position p
        à l'intérieur de la zone de jeu L
        et que la position ne coïncide pas avec
        un mur.
        p = position possible du personnage
        '''
        return (p.x > len(L[0])) or (p.x < 0) or (p.y < 0) or (p.y > len(L)) or (L[p.y][p.x] == 'I')

    def deplacement(self, c, L):
        '''
        Méthode qui contrôle le déplacement
        du personnage dans la zone du jeu L
        c = une chaîne de caractère qui prend les
        valeurs (G, D, H, B, Q)
        Si le déplacement est impossible, la méthode
        ne retourne rien, et si l'utilisateur choisit
        Q (Quitter), on quitte le jeu.
        '''
        x, y = self.x, self.y
        haut = Point(x, y-1)
        droite = Point(x+1, y)
        bas = Point(x, y+1)
        gauche = Point(x-1, y)
        if c == curses.KEY_UP and not(self.verification_deplacement(haut, L)):
            L[y][x], L[y-1][x] = ' ', self.pers
            self.x, self.y = x, y-1
            return L
        elif c == curses.KEY_RIGHT and not(self.verification_deplacement(droite, L)):
            L[y][x], L[y][x+1] = ' ', self.pers
            self.x, self.y = x+1, y
            return L
        elif c == curses.KEY_DOWN and not(self.verification_deplacement(bas, L)):
            L[y][x], L[y+1][x] = ' ', self.pers
            self.x, self.y = x, y+1
            return L
        elif c == curses.KEY_LEFT and not(self.verification_deplacement(gauche, L)):
            L[y][x], L[y][x-1] = ' ', self.pers
            self.x, self.y = x-1, y
            return L
        elif c == 27:
            os._exit(1)
        else:
            return None


if __name__ == '__main__':
    print(9)

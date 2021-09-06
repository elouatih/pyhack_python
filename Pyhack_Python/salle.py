#!/usr/bin/python3
"""
Le fichier salle.py crée un objet Salle
en indiquant les coordonnées du point
haut_gauche de la salle, sa largeur et
sa hauteur.
"""
from random import randint, choice
from point import Point


class Salle(Point):
    '''
    Cette classe, qui hérite de la classe Point,
    permet d'afficher des salles et les relier par
    des couloirs dans un donjon représenté ici
    par une liste en 2 dimensions appelée 'plateforme'
    '''
    def __init__(self, x, y, largeur, hauteur):
        '''
        Les paramètres de l'object Salle sont :
        (x, y) : les coordonnées du point le plus
                  haut à gauche de la salle
        largeur : largeur de la Salle
        hauteur : hauteur de la Salle
        '''
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur

# Partie Salle

    def afficher_salle(self, plateforme):
        '''
        Le fait d'afficher une salle consiste à
        vider l'intérieur de l'espace contouré par
        les dimensions de la salle.
        La méthode prend en argument une liste et renvoie
        la liste mutée.
        '''
        for i in range(self.y, self.y + self.hauteur + 1):
            for j in range(self.x, self.x + self.largeur + 1):
                plateforme[i][j] = ' '
        return plateforme

# Partie Couloir
    '''
    Cette partie permet de lier des salles
    par des couloirs aléatoires.
    Nous avons conçu un couloir aléatoire
    comme étant un chemin qui lie deux points
    aléatoires appartenant à la bordure de deux listes.
    '''

    def point_bordure(self):
        '''
        Le point_bordure est un point aléatoire
        qui appartient à la bordure de la salle.
        Nord, Sud, Ouest et Est seront alors des points tirés
        aléatoirement des quatres côtés de la salle.
        Nous tirerons alors un point parmi ces quatre points
        '''
        nord = Point(randint(self.x, self.x + self.largeur), self.y)
        est = Point(self.x + self.largeur, randint(self.y, self.y + self.hauteur))
        sud = Point(randint(self.x, self.x + self.largeur), self.y + self.hauteur)
        ouest = Point(self.x, randint(self.y, self.y + self.hauteur))
        liste_points_bordure = [nord, est, sud, ouest]
        return choice(liste_points_bordure)

    def tracer_couloir(self, point1, point2, plateforme):
        """
        Cette méthode, d'abord va tracer un couloir entre deux
        points quelconques du plan, soit les deux points
        point1, point2
        """
        for n in range(min(point1.x, point2.x), max(point1.x, point2.x) + 1):
            plateforme[point1.y][n] = ' '
        for m in range(min(point1.y, point2.y), max(point1.y, point2.y) + 1):
            plateforme[m][point2.x] = ' '
        return plateforme

    def liaison_couloir(self, salle1, plateforme):
        '''
        Cette méthode se sert de la méthode tracer_couloir
        pour lier deux salles.
        Les points choisis sont deux points_bordures des salles.
        '''
        point1 = self.point_bordure()
        point2 = salle1.point_bordure()
        self.tracer_couloir(point1, point2, plateforme)


if __name__ == '__main__':
    print(8)

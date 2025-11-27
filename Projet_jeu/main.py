#importer le module pygame
import pygame

#importer les modules pytmx et pyscroll (pour l'affichage de la carte)
import pytmx
import pyscroll

from game import Game

#charger le module pygame
pygame.init()

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    
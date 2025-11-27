import pygame
import pyscroll
import pytmx

from player import Player

class Game:
    def __init__(self):
        #générere la fenêtre du jeu:
        #-nom de la fenêtre de l'app et icon (titre, icon)
        pygame.display.set_caption("Tower Adventure")
        #-taille de la fenêtre de l'app (largeur, hauteur)
        self.screen = pygame.display.set_mode((1080,720))

        #importer et charger l'arriere plan (mettre le chemin relatif entre les "")
        #background = pygame.image.load("map.tmx")

        #charger la carte (format tmx)
        tmx_data = pytmx.util_pygame.load_pygame("map.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        
        #générer le joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)
        
        #dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=100)
        #Pour le joueur
        self.group.add(self.player)

    def handle_input(self):
        #récupérer les inputs du joueur
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z] and pressed[pygame.K_s] or pressed[pygame.K_q] and pressed[pygame.K_d]:
            None
        #elif pressed[pygame.K_z] and pressed[pygame.K_q]:
        #    self.player.move_top_left()                                  
        #elif pressed[pygame.K_z] and pressed[pygame.K_d]:
        #    self.player.move_top_right()
        #elif pressed[pygame.K_s] and pressed[pygame.K_q]:
        #    self.player.move_bottom_left()                                
        #elif pressed[pygame.K_s] and pressed[pygame.K_d]:
        #    self.player.move_bottom_right()
        elif pressed[pygame.K_z]:
            self.player.move_up()
            self.player.change_animation("up")
        elif pressed[pygame.K_s]:
            self.player.move_down()
            self.player.change_animation("down")
        elif pressed[pygame.K_q]:
            self.player.move_left()
            self.player.change_animation("left")
        elif pressed[pygame.K_d]:
            self.player.move_right()
            self.player.change_animation("right")


    def run(self):

        #definition des fps du jeu
        clock = pygame.time.Clock()

        #maintien de la fenêtre ouverte tant que la boucle est vraie
        running = True
        while running:

            self.handle_input()
            self.group.update()
            self.group.center(self.player.rect.center)
            #application de l'arriere plan du jeu
            #screen.blit(background, (0,0))
            self.group.draw(self.screen)
            #mettre à jour la fenêtre
            pygame.display.flip()

            #si le joueur ferme la fenêtre et bien elle se ferme XD
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            clock.tick(60)
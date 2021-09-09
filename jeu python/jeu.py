from joueur import Joueur
from mob import Mob
import pygame
#creer une classe game qui va representer le jeu

class Jeu:
    def __init__(self):
        self.playersGroup = pygame.sprite.Group() #pour gerer les collisions avec les aubergines ou autres
        #generer notre joueur
        self.player = Joueur(self)
        self.playersGroup.add(self.player)
        #groupe de monstre
        self.aubergines = pygame.sprite.Group()
        self.pressed = {}
        self.counter = 0
        for i in range(1, 3)
              self.creer_aubergine()
        self.n_aubergines_detruites = 0
        self.boss_lvl1 = False
        self.boss_lvl1_detruit = False
        self.lvl2_started = False
        self.boss_lvl2_detruit = False
        self.check_n = -100

    def lvl2_mob_spawn(self):
       for i in range(1, 3)
              self.creer_aubergine()
        self.lvl2_started = True

    def boss_lvl1_active(self):
        self.boss_lvl1 = True

    def aubergine_detruite(self):
        self.n_aubergines_detruites += 1

    def create_boss(self):
        boss = Mob(self)
        boss.est_un_boss = True
        boss.rect.y = 200
        boss.points_de_vie = 200
        boss.vitesse = 3
        self.aubergines.add(boss)

    def create_boss2(self):
        boss = Mob(self)
        boss.est_un_boss = True
        boss.rect.y = 200
        boss.points_de_vie = 250
        boss.vitesse = 3
        boss.image = pygame.image.load("images/boss_lvl1.png")
        self.aubergines.add(boss)

    def remove_aubergines(self):
        self.aubergines.empty()

    def creer_aubergine(self):
        a = Mob(self)
        self.aubergines.add(a)

    def touched(self, sprite, group):#gere les collisions
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

import pygame
import random
from pygame import mixer

#creer la classe monstre

class Mob(pygame.sprite.Sprite):

    def __init__(self, Jeu):
        super().__init__()
        self.j = Jeu #j est l'instance de la game en cours
        self.points_de_vie = 100
        self.max_points_de_vie = 100
        self.attaque = 0.8
        self.image = pygame.image.load('images/aubergine.png')
        self.rect = self.image.get_rect()
        self.rect.x = 600 + random.randint(0, 400)
        self.rect.y = 520
        self.vitesse = random.randint(3, 8)
        self.boss_lvl1_genere = False
        self.boss_lvl2_genere = False
        self.boss_lvl1 = False
        self.boss_lvl2 = False
        self.left = False
        self.right = False
        self.compteur_pas = 0
        self.est_un_boss = False

    def fonce_vers_joueur(self):

        if self.est_un_boss:
            self.rect.y = 500

        if not self.est_un_boss:
            aubergine_a_gauche = [pygame.image.load('images/petit_pois_walk_1.png')
                , pygame.image.load('images/petit_pois_2.png')
                , pygame.image.load('images/petit_pois_walk_3.png')
                , pygame.image.load('images/petit_pois_walk_1.png')
                , pygame.image.load('images/petit_pois_2.png')
                , pygame.image.load('images/petit_pois_walk_3.png')
                , pygame.image.load('images/petit_pois_walk_1.png')
                , pygame.image.load('images/petit_pois_2.png')
                , pygame.image.load('images/petit_pois_walk_3.png')]
        if self.est_un_boss:

            aubergine_a_gauche = [pygame.image.load('images/boss1.png')
                , pygame.image.load('images/boss2.png')
                , pygame.image.load('images/boss3.png')
                , pygame.image.load('images/boss1.png')
                , pygame.image.load('images/boss2.png')
                , pygame.image.load('images/boss3.png')
                , pygame.image.load('images/boss1.png')
                , pygame.image.load('images/boss2.png')
                , pygame.image.load('images/boss3.png')]



        if self.compteur_pas > 5:
            self.compteur_pas = 0
        else:
            self.image = aubergine_a_gauche[self.compteur_pas // 2]
            self.image = pygame.transform.scale(self.image, (200, 210))
            self.compteur_pas += 1

        if not self.j.touched(self, self.j.playersGroup):
            self.rect.x -= self.vitesse
        else:
            #Infliger des degats en cas de collision si c'est possible
            self.j.player.degats(self.attaque)

    def degats(self, d):
            self.points_de_vie -= d

            if self.points_de_vie <= 0:
                if self.boss_lvl2_genere:
                    self.j.remove_aubergines()

                if self.j.lvl2_started and self.j.n_aubergines_detruites == 20 and not self.boss_lvl2_genere:
                    self.j.remove_aubergines()
                    self.boss_lvl2_genere = True
                    if not self.j.boss_lvl2_detruit:
                        self.j.create_boss2()
                        self.j.check_n = self.j.n_aubergines_detruites + 1

                if self.j.boss_lvl1 and not self.j.boss_lvl1_detruit:
                    self.j.remove_aubergines()
                    self.j.boss_lvl1_detruit = True
                    self.j.lvl2_started = True
                self.j.aubergine_detruite()
                if self.j.n_aubergines_detruites == 10  and not self.boss_lvl1_genere:
                    self.j.remove_aubergines()
                    self.j.create_boss()
                    self.j.boss_lvl1_active()
                    self.boss_lvl1_genere = True
                self.rect.x += 1000 + random.randint(0, 400) #un monstre va spwan avec un decalage de 1000 en x plus loin
                self.points_de_vie = self.max_points_de_vie
                if self.j.lvl2_started:
                    self.vitesse = random.randint(8, 12)
                else:
                    self.vitesse = random.randint(5, 8)

import pygame
from pepin import Pepin
from pygame import mixer

class Joueur(pygame.sprite.Sprite):

    def __init__(self, jeu):
        super().__init__()
        self.j = jeu
        self.points_de_vie = 100
        self.max_points_de_vie = 100
        self.attaque = 5
        self.vitesse = 8
        self.pepins = pygame.sprite.Group()
        self.image = pygame.image.load('images/tomate2.png')
        self.image = pygame.transform.scale(self.image, (200, 210))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 500

    def lancer_pepin(self):
        self.bruit_pepin = mixer.Sound("sound_effects/laser.wav")
        self.bruit_pepin.play()
        self.pepins.add(Pepin(self))

    def bouger_a_droite(self):
    #si le joueur n'est pas en collision
        if not self.j.touched(self, self.j.aubergines):
            self.rect.x += self.vitesse

    def bouger_a_gauche(self):
        self.rect.x -= self.vitesse

    def degats(self, d):
        if self.points_de_vie - d > d:
            self.points_de_vie -= d
        else:
            self.points_de_vie = 0
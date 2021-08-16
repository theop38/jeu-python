import pygame

class Pepin(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.vitesse = 8
        self.player = player
        self.image = pygame.image.load('images/pepin.png')
        self.image = pygame.transform.scale(self.image, (35, 20))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 135
        self.rect.y = player.rect.y + 115
        self.image_origine = self.image
    def remove(self):
        self.player.pepins.remove(self)

    def move(self):
        self.rect.x += self.vitesse

        #verifier si le pepin entre en collision avec une aubergine
        for aubergine in self.player.j.touched(self, self.player.j.aubergines):
            self.remove()
            #on connait la liste des aubergines qui ont été impacté
            #on peut donc infliger des degats
            aubergine.degats(7)

        if self.rect.x > 900:
            self.remove() 
import pygame
from jeu import Jeu
from pygame import mixer
from gamemenu import GameMenu

pygame.init()
clock = pygame.time.Clock()
g = GameMenu()


mixer.music.load('sound_effects/yellow_mellow.mp3') #yellow
mixer.music.play(-1) #-1 pour dire que ça joue en boucle

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
    if g.user_choice:
        break

fenetre = pygame.display.set_mode((1024, 768))
jouer = False
credit = False

if g.choix_jouer:
    jouer = True
elif g.choix_credit:
    credit = True
else:
    pygame.quit()

game_over = False
decor = pygame.image.load('images/sp_b.png')
game = Jeu()
jump = False

marcher_a_droite = [  pygame.image.load('images/tomate1.png')
                    , pygame.image.load('images/tomate2.png')
                    , pygame.image.load('images/tomate3.png')
                    , pygame.image.load('images/tomate1.png')
                    , pygame.image.load('images/tomate2.png')
                    , pygame.image.load('images/tomate3.png')
                    , pygame.image.load('images/tomate1.png')
                    , pygame.image.load('images/tomate2.png')
                    , pygame.image.load('images/tomate3.png')]

marcher_a_gauche = [  pygame.image.load('images/tomate1.png')
                    , pygame.image.load('images/tomate2.png')
                    , pygame.image.load('images/tomate3.png')
                    , pygame.image.load('images/tomate1.png')
                    , pygame.image.load('images/tomate2.png')
                    , pygame.image.load('images/tomate3.png')
                    , pygame.image.load('images/tomate1.png')
                    , pygame.image.load('images/tomate2.png')
                    , pygame.image.load('images/tomate3.png')]

marcher_a_droite_dodo = [  pygame.image.load('images/tomate_dodo1.png')
                    , pygame.image.load('images/tomate_dodo2.png')
                    , pygame.image.load('images/tomate_dodo3.png')
                    , pygame.image.load('images/tomate_dodo1.png')
                    , pygame.image.load('images/tomate_dodo2.png')
                    , pygame.image.load('images/tomate_dodo3.png')
                    , pygame.image.load('images/tomate_dodo1.png')
                    , pygame.image.load('images/tomate_dodo2.png')
                    , pygame.image.load('images/tomate_dodo3.png')]

marcher_a_gauche_dodo = [  pygame.image.load('images/tomate_dodo1.png')
                    , pygame.image.load('images/tomate_dodo2.png')
                    , pygame.image.load('images/tomate_dodo3.png')
                    , pygame.image.load('images/tomate_dodo1.png')
                    , pygame.image.load('images/tomate_dodo2.png')
                    , pygame.image.load('images/tomate_dodo3.png')
                    , pygame.image.load('images/tomate_dodo1.png')
                    , pygame.image.load('images/tomate_dodo2.png')
                    , pygame.image.load('images/tomate_dodo3.png')]

i = 0
width = decor.get_width()
left = False
right = False
compteur_pas = 0
hauteur_perso = 230
largeur_perso = 320
boss_lvl1_spawn = False
lvl_2 = False

font=pygame.font.Font("fonts/Pangolin-Regular.ttf", 43)
c = False

def redessiner_fenetre_jeu():
    score = font.render("Score: " + str(game.n_aubergines_detruites), 1, (255, 255, 255))
    vie = font.render("Vie: " + str(game.player.points_de_vie.__floor__()), 1, (255, 255, 255))
    global compteur_pas
    global decor
    global lvl_2
    global game_over
    global credit
    global c

    if game.check_n == game.n_aubergines_detruites and not c:
        mixer.music.load('sound_effects/Red_Soup.mp3')
        mixer.music.play(-1)
        c = True

    if game.check_n + 1 == game.n_aubergines_detruites:
        pygame.time.wait(50)
        game.boss_lvl2_detruit = True

    if game.boss_lvl1_detruit and not lvl_2:
        decor = pygame.image.load("images/bg2.png")
        lvl_2 = True
        #ici blue_bounce_sleep
        mixer.music.load('sound_effects/blue_bounce_sleep.mp3')
        mixer.music.play(-1)
        game.lvl2_mob_spawn()
    elif game.player.points_de_vie == 0:
        game_over = True
    if game.n_aubergines_detruites == 9:
        credit = True

    fenetre.fill((0, 0, 0))
    fenetre.blit(decor, (0, 0))
    fenetre.blit(decor, (i, 0))
    fenetre.blit(decor, (width + i, 0))
    fenetre.blit(score, (0, 0))
    fenetre.blit(vie, (0, 50))

    if compteur_pas > 26:
        compteur_pas = 0
    if right:
        if not game.lvl2_started:
            marcher_a_droite[compteur_pas//3] = pygame.transform.scale(marcher_a_droite[compteur_pas//3], (200, 210))
            fenetre.blit(marcher_a_droite[compteur_pas//3], game.player.rect)
        else:
            marcher_a_droite_dodo[compteur_pas // 3] = pygame.transform.scale(marcher_a_droite_dodo[compteur_pas // 3], (200, 210))
            fenetre.blit(marcher_a_droite_dodo[compteur_pas // 3], game.player.rect)
        compteur_pas += 1
    elif left:
        if not game.lvl2_started:
            marcher_a_gauche[compteur_pas // 3] = pygame.transform.scale(marcher_a_droite[compteur_pas // 3], (200, 210))
            fenetre.blit(marcher_a_gauche[compteur_pas //3], game.player.rect)
        else:
            marcher_a_gauche_dodo[compteur_pas // 3] = pygame.transform.scale(marcher_a_gauche_dodo[compteur_pas // 3],(200, 210))
            fenetre.blit(marcher_a_gauche_dodo[compteur_pas // 3], game.player.rect)
        compteur_pas += 1
    else:
        if not game.lvl2_started:
            fenetre.blit(game.player.image, game.player.rect)
        else:
            im = pygame.transform.scale(marcher_a_gauche_dodo[2], (200, 210))
            fenetre.blit(im, game.player.rect)

musique_boss1 = False
mg = False

while jouer:
    clock.tick(100)
    redessiner_fenetre_jeu()
    if not mg:
        mixer.music.load('sound_effects/Mean_Green.mp3')  # mean grean
        mixer.music.play(-1)  # -1 pour dire que ça joue en boucle
        mg = True
    if game.boss_lvl1 == True and musique_boss1 == False:
        musique_boss1 = True
        mixer.music.load('sound_effects/purple_trouble.mp3')
        mixer.music.play(-1)
    if i == -width:
        fenetre.blit(decor, (width + i, 0))
        i = 0
    i -= 1

    for projectile in game.player.pepins:
        projectile.move()

    game.player.pepins.draw(fenetre)

    for aubergine in game.aubergines:
        aubergine.fonce_vers_joueur()

    game.aubergines.draw(fenetre)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 750:
        right = True
        left = False
        game.player.bouger_a_droite()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -50:
        right = False
        left = True
        game.player.bouger_a_gauche()
    else:
        right = False
        left = False
        compteur_pas = 0

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jouer = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.lancer_pepin()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    if game.boss_lvl2_detruit:
        credit = True
        jouer = False
    if game_over:
        jouer = False
        break

credit = font.render("Credit", 1, (255,255,255))
TiltGang = font.render("-----------:", 1, (255,255,255))
theo = font.render("--------- : Programmer", 1, (255,255,255))
antoine = font.render("------- : Background artist and programmer", 1, (255,255,255))
moyad = font.render("---------------- : Lead game designer", 1, (255,255,255))
nicolas = font.render("---------------- : Narrative director and animator", 1, (255,255,255))
help = font.render("#With the help of :", 1, (255,255,255))
starchild = font.render("------------- : Composer", 1, (255,255,255))
kylpet = font.render("----------- : Character artist", 1, (255,255,255))

if game_over:
    decor = pygame.image.load('images/game_over.png')
    pygame.display.update()
    mixer.music.stop()

while game_over:
    fenetre.fill((0,0,0))
    fenetre.blit(decor, (0,0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
           game_over = False
           credit = False
           pygame.quit()
s = 0


mixer.music.load('sound_effects/background.wav') #mean grean
mixer.music.play(-1) #-1 pour dire que ça joue en boucle


while credit:
    fenetre.fill((0,0,0))
    fenetre.blit(credit, (0,s))
    fenetre.blit(TiltGang, (0, s + 50))
    fenetre.blit(theo, (0, s + 100))
    fenetre.blit(antoine, (0, s + 150))
    fenetre.blit(moyad, (0, s + 200))
    fenetre.blit(nicolas, (0, s + 250))
    fenetre.blit(help, (0, s + 300))
    fenetre.blit(starchild, (0, s + 350))
    fenetre.blit(kylpet, (0, s + 400))
    s += 1
    pygame.time.wait(100)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            credit = False
            pygame.quit()

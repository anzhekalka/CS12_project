from classes import *
import sys

def level1(location):
    if location == 'r':
        location = 75
    elif location == 'l':
        location = 1325
    player = PLayer((location, 525), player_img)

    hitbox_floor = Images(hitbox_img, (WIDTH / 2, 597))
    obstacles_group = pygame.sprite.Group()
    obstacles_group.add(hitbox_floor)

    floor_1 = Images(level1_floor_img, (WIDTH / 2, HEIGHT / 2))
    level1_images_gr = pygame.sprite.Group()
    level1_images_gr.add(floor_1)

    objet_group = pygame.sprite.Group()
    objet_group.add(player)
    clock = pygame.time.Clock()
    min_fps = 200
    while True:

        SCREEN.blit(level1_back_img, (0, 0))
        obstacles_group.draw(SCREEN)
        objet_group.draw(SCREEN)
        level1_images_gr.draw(SCREEN)
        pygame.display.flip()

        if player.rect.centerx > WIDTH:
            return([2, 'r'])
        player.update(12, obstacles_group)
        player.falling(obstacles_group)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        if min_fps > clock.get_fps() > 0:
            min_fps = clock.get_fps()

        clock.tick(FPS)

def level2(location):
    if location == 'r':
        location = 50
    elif location == 'l':
        location = 1325
    start_y_buffer = 565
    player = PLayer((location, start_y_buffer), player_img)

    hitbox1_floor = Images(hitbox1_lvl2_img, (201, 635))
    hitbox2_floor = Images(hitbox2_lvl2_img, (980, 635))
    roof_hitbox = Images(hitbox_img, (WIDTH/ 2, 138))
    barrier1 = Images(barrier1_lvl2, (284, 580))
    barrier2 = Images(barrier2_lvl2, (700, 557))
    barrier3 = Images(barrier3_lvl2, (985, 509))
    barrier4 = Images(barrier4_lvl2, (1221, 535))
    barrier5 = Images(barrier5_lvl2, (171, 377))
    barrier6 = Images(barrier6_lvl2, (124, 347))
    barrier7 = Images(barrier7_lvl2, (54, 233))
    obstacles_group = pygame.sprite.Group()
    obstacles_group.add(barrier1, barrier2, barrier3, barrier4, barrier5, barrier6, barrier7)
    obstacles_group.add(hitbox1_floor, hitbox2_floor, roof_hitbox)

    floor = Images(level2_floor_img, (WIDTH / 2, HEIGHT / 2))
    level2_images_gr = pygame.sprite.Group()
    level2_images_gr.add(floor)

    danger1 = Images(danger1_lvl2, (505, 652))
    danger_group = pygame.sprite.Group()
    danger_group.add(danger1)

    objet_group = pygame.sprite.Group()
    objet_group.add(player)
    clock = pygame.time.Clock()
    min_fps = 200
    while True:
        SCREEN.blit(level2_back_img, (0, 0))
        obstacles_group.draw(SCREEN)
        objet_group.draw(SCREEN)
        level2_images_gr.draw(SCREEN)
        pygame.display.flip()

        if player.rect.centerx < 0:
            return([1, 'l'])

        player.falling(obstacles_group)
        player.update(12, obstacles_group)
        player.dying(danger_group, location, start_y_buffer)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        if min_fps > clock.get_fps() > 0:
            min_fps = clock.get_fps()

        clock.tick(FPS)

def game():
    x = level1('r')
    while True:
        if x[0] == 2:
            x = level2(x[1])
        elif x[0] == 1:
            x = level1(x[1])





def main_menu():

    # pygame.mixer.music.load(menu_fon_music)
    # pygame.mixer.music.set_volume(music_volume)
    # pygame.mixer.music.play(-1)

    pygame.display.set_caption("GAME")

    play_btn = Button(play_btn_img, (WIDTH / 2, HEIGHT * 0.44))
    #options_btn = Button(options_btn_img, (WIDTH / 2, HEIGHT * 0.33))
    exit_btn = Button(exit_btn_img, (WIDTH / 2, HEIGHT * 0.66))
    heading_img = Images(heading_menu_img, (WIDTH / 2, HEIGHT * 0.12))

    buttons_gr = pygame.sprite.Group()
    images_gr = pygame.sprite.Group()
    buttons_gr.add(play_btn, exit_btn)
    images_gr.add(heading_img)

    SCREEN.blit(fon_img, (100, 0))
    buttons_gr.draw(SCREEN)
    images_gr.draw(SCREEN)

    pygame.display.flip()
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_btn.rect.collidepoint(mouse_pos):
                    SCREEN.blit(fon_img, (0, 0))
                    game()
                elif exit_btn.rect.collidepoint(mouse_pos):
                    sys.exit()

main_menu()


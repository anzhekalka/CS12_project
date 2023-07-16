from classes import *
import sys
import random

def game():
    player = PLayer((WIDTH * 0.1, HEIGHT * 0.67), player_img)
    level_counter = 1
    text_level1 = font_text.render("LEVEL " + str(level_counter), False, (249, 246, 238))
    text_rect = (WIDTH / 2 - 50, HEIGHT * 0.05)

    exit_btn = Button(exit2_btn_img, (WIDTH * 0.1, HEIGHT * 0.075))

    obstacles_group = pygame.sprite.Group()
    load_level(obstacles_group)

    objet_group = pygame.sprite.Group()
    objet_group.add(player, exit_btn)
    clock = pygame.time.Clock()
    min_fps = 200

    while True:
        SCREEN.blit(fon_game_img, (0, 0))
        SCREEN.blit(text_level1, text_rect)
        objet_group.draw(SCREEN)
        obstacles_group.draw(SCREEN)
        pygame.display.flip()

        player.update(obstacles_group)
        if player.rect.left>WIDTH:
            player.rect.center = (WIDTH * 0.1, HEIGHT * 0.67)
            load_level(obstacles_group)
            level_counter += 1
            #список фонов
            #fon_game_img = randon.choice ()

            text_level1 = font_text.render("LEVEL " + str(level_counter), False, (249, 246, 238))
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if exit_btn.rect.collidepoint(mouse_pos):
                    main_menu()

        if min_fps > clock.get_fps() > 0:
            min_fps = clock.get_fps()
        print(f"Фактическое кол-во FPS = {clock.get_fps()} а минимальное = {min_fps}")
        clock.tick(FPS)


def load_level(obstacles_group):
    for element in obstacles_group:
        element.kill()
    for i in range (6):
        obstacles_group.add(Obstacles(0, (random.randint(100, WIDTH), HEIGHT * 0.67)))


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
    images_gr= pygame.sprite.Group()
    buttons_gr.add(play_btn, exit_btn)
    images_gr.add(heading_img)

    SCREEN.blit(fon_img, (0, 0))
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

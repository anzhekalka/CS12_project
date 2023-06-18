from classes import *
import sys


def game():
    player = PLayer((WIDTH / 2, HEIGHT / 2))

    text_game = font_text.render("Game", False, (0, 0, 0))
    text_rect = text_game.get_rect()
    text_rect = (150, 150)


    objet_group = pygame.sprite.Group()
    objet_group.add(player)
    clock = pygame.time.Clock()
    min_fps = 200
    while True:
        SCREEN.blit(fon_img, (0, 0))
        SCREEN.blit(text_game, text_rect)
        objet_group.draw(SCREEN)
        pygame.display.flip()
        mouse_pos = pygame.mouse.get_pos()

        player.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if min_fps > clock.get_fps() > 0:
            min_fps = clock.get_fps()
        print(f"Фактическое кол-во FPS = {clock.get_fps()} а минимальное = {min_fps}")
        clock.tick(FPS)


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

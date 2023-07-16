import os
import pygame

WIDTH = 1200
HEIGHT = 800
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 200

main_folder = os.path.dirname(__file__)
image_folder = os.path.join(main_folder, "image")
buttons_img_folder = os.path.join(image_folder, "buttons")
background_img_folder = os.path.join(image_folder, "background")
sound_folder = os.path.join(main_folder, "sound")
font_folder = os.path.join(main_folder, "font")

fon_img = pygame.image.load(os.path.join(background_img_folder, "fon.jpg")).convert_alpha()
fon_game_img = pygame.image.load(os.path.join(background_img_folder, "fon_game.jpg")).convert_alpha()
player_img = pygame.image.load(os.path.join(main_folder, "image/character_official.png"))
play_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "play.png")).convert_alpha()
options_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "options.png")).convert_alpha()
exit_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "exit.png")).convert_alpha()
exit2_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "exit3.png")).convert_alpha()
heading_menu_img = pygame.image.load(os.path.join(main_folder, "image/heading.png")).convert_alpha()
brick_img = pygame.image.load(os.path.join(main_folder, "image/brick.png")).convert_alpha()
obstacles_list = [exit2_btn_img]

font_file = os.path.join(font_folder, "Montserrat.ttf")
font_text = pygame.font.Font(font_file, 40)

# menu music and sounds
menu_fon_music = os.path.join(sound_folder, "music_fon_menu.mp3")

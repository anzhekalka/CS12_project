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
player_img = pygame.image.load(os.path.join(image_folder, "character_official.png")).convert_alpha()
play_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "play.png")).convert_alpha()
options_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "options.png")).convert_alpha()
exit_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "exit.png")).convert_alpha()
heading_menu_img = pygame.image.load(os.path.join(image_folder, "heading.png")).convert_alpha()
level1_back_img = pygame.image.load(os.path.join(background_img_folder, "level1_part1_back.png")).convert_alpha()
level1_floor_img = pygame.image.load(os.path.join(background_img_folder, "level1_part1_floor.png")).convert_alpha()
hitbox_img = pygame.image.load(os.path.join(image_folder, "floor_hitbox.png")).convert_alpha()
player_big_img = pygame.image.load(os.path.join(image_folder, "character_big.png")).convert_alpha()

font_file = os.path.join(font_folder, "Dune_Rise.ttf")
font_text = pygame.font.Font(font_file, 40)

# menu music and sounds
menu_fon_music = os.path.join(sound_folder, "music_fon_menu.mp3")

import os
import pygame

WIDTH = 600
HEIGHT = 600
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
player_img = pygame.image.load(os.path.join(buttons_img_folder, "play.png")).convert_alpha()
play_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "play.png")).convert_alpha()
options_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "options.png")).convert_alpha()
exit_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "exit.png")).convert_alpha()

font_file = os.path.join(font_folder, "image/Dune_Rise.ttf")
font_text = pygame.font.Font(font_file, 40)

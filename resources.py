import os
import pygame

WIDTH = 1400
HEIGHT = 800
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 30

main_folder = os.path.dirname(__file__)
image_folder = os.path.join(main_folder, "image")
buttons_img_folder = os.path.join(image_folder, "buttons")
background_img_folder = os.path.join(image_folder, "background")
animation_folder = os.path.join(image_folder, "animation")
sound_folder = os.path.join(main_folder, "sound")
font_folder = os.path.join(main_folder, "font")

#меню
fon_img = pygame.image.load(os.path.join(background_img_folder, "fon.jpg")).convert_alpha()
play_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "play.png")).convert_alpha()
options_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "options.png")).convert_alpha()
exit_btn_img = pygame.image.load(os.path.join(buttons_img_folder, "exit.png")).convert_alpha()
heading_menu_img = pygame.image.load(os.path.join(image_folder, "heading.png")).convert_alpha()
#уровень 1
level1_back_img = pygame.image.load(os.path.join(background_img_folder, "level1_part1_back.png")).convert_alpha()
level1_floor_img = pygame.image.load(os.path.join(background_img_folder, "level1_part1_floor.png")).convert_alpha()
hitbox_img = pygame.image.load(os.path.join(image_folder, "floor_hitbox.png")).convert_alpha()
#уровень 2
barrier1_lvl2 = pygame.image.load(os.path.join(background_img_folder, "level2/barrier_hitbox1_lvl2.png")).convert_alpha()
barrier2_lvl2 = pygame.image.load(os.path.join(background_img_folder, "level2/barrier_hitbox2_lvl2.png")).convert_alpha()
barrier3_lvl2 = pygame.image.load(os.path.join(background_img_folder, "level2/barrier_hitbox3_lvl2.png")).convert_alpha()
barrier4_lvl2 = pygame.image.load(os.path.join(background_img_folder, "level2/barrier_hitbox4_lvl2.png")).convert_alpha()
barrier5_lvl2 = pygame.image.load(os.path.join(background_img_folder, "level2/barrier_hitbox5_lvl2.png")).convert_alpha()
barrier6_lvl2 = pygame.image.load(os.path.join(background_img_folder, "level2/barrier_hitbox6_lvl2.png")).convert_alpha()
barrier7_lvl2 = pygame.image.load(os.path.join(background_img_folder, "level2/barrier_hitbox7_lvl2.png")).convert_alpha()
level2_back_img = pygame.image.load(os.path.join(background_img_folder, "level2/level2_background.png")).convert_alpha()
level2_floor_img = pygame.image.load(os.path.join(background_img_folder, "level2/level2_floor.png")).convert_alpha()
hitbox1_lvl2_img = pygame.image.load(os.path.join(background_img_folder, "level2/floor_hitbox1_lvl2.png")).convert_alpha()
hitbox2_lvl2_img = pygame.image.load(os.path.join(background_img_folder, "level2/danger_hitbox2_lvl2.png")).convert_alpha()
danger1_lvl2 = pygame.image.load(os.path.join(background_img_folder, "level2/floor_hitbox2_lvl2.png")).convert_alpha()

player_big_img = pygame.image.load(os.path.join(image_folder, "character_big.png")).convert_alpha()
player_img = pygame.image.load(os.path.join(image_folder, "character_official.png")).convert_alpha()
#анимация на прыжок
player_img_j1 = pygame.image.load(os.path.join(animation_folder, "jump/characters_jump1.png")).convert_alpha()
player_img_j2 = pygame.image.load(os.path.join(animation_folder, "jump/characters_jump2.png")).convert_alpha()
player_img_j3 = pygame.image.load(os.path.join(animation_folder, "jump/characters_jump3.png")).convert_alpha()
player_img_j4 = pygame.image.load(os.path.join(animation_folder, "jump/characters_jump4.png")).convert_alpha()
player_img_j5 = pygame.image.load(os.path.join(animation_folder, "jump/characters_jump5.png")).convert_alpha()
#анимация на ходьбу
player_img_go1 = pygame.image.load(os.path.join(animation_folder, "going/character_going1.png")).convert_alpha()
player_img_go2 = pygame.image.load(os.path.join(animation_folder, "going/character_going2.png")).convert_alpha()
player_img_go3 = pygame.image.load(os.path.join(animation_folder, "going/character_going3.png")).convert_alpha()
player_img_go4 = pygame.image.load(os.path.join(animation_folder, "going/character_going4.png")).convert_alpha()

font_file = os.path.join(font_folder, "Dune_Rise.ttf")
font_text = pygame.font.Font(font_file, 40)

# menu music and sounds
menu_fon_music = os.path.join(sound_folder, "music_fon_menu.mp3")

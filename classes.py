import pygame

from resources import *



class Button(pygame.sprite.Sprite):
    def __init__(self, img_file, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img_file
        self.rect = self.image.get_rect()
        self.rect.center = pos
class Images(pygame.sprite.Sprite):
    def __init__(self, img_file, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img_file
        self.rect = self.image.get_rect()
        self.rect.center = pos

class PLayer(pygame.sprite.Sprite):
    def __init__(self, pos, image_to_put):
        pygame.sprite.Sprite.__init__(self)
        self.put = image_to_put
        self.image = self.put
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.is_left = True
        self.is_jump = False
        self.is_falling = False
        self.phase = 0
        self.shadow = Images(player_img, pos)
        self.jump_direction = 0
        self.is_just_fall = False
        self.phase_going = 0
        #self.shadow = Images(image_to_put, pos)

    def animation_going(self):
        if 0 <= self.phase_going <= 9:
            if self.is_left:
                self.image = self.put
            else:
                self.image = pygame.transform.flip(self.put, True, False)
        elif 10 <= self.phase_going <= 19:
            if self.is_left:
                self.image = player_img_go1
            else:
                self.image = pygame.transform.flip(player_img_go1, True, False)
        elif 20 <= self.phase_going <= 29:
            if self.is_left:
                self.image = player_img_go2
            else:
                self.image = pygame.transform.flip(player_img_go2, True, False)
        if 30 <= self.phase_going <= 39:
            if self.is_left:
                self.image = player_img_go3
            else:
                self.image = pygame.transform.flip(player_img_go3, True, False)
        if 40 <= self.phase_going <= 49:
            if self.is_left:
                self.image = player_img_go4
            else:
                self.image = pygame.transform.flip(player_img_go4, True, False)

        self.phase_going += 1
        if self.phase_going == 50:
            self.phase_going = 0

    def animation_falling(self):
        if self.phase < 3 and self.is_jump:
            if self.is_left:
                self.image = player_img_j1
            else:
                self.image = pygame.transform.flip(player_img_j1, True, False)
        elif self.phase < 6 and self.is_jump:
            if self.is_left:
                self.image = player_img_j2
            else:
                self.image = pygame.transform.flip(player_img_j2, True, False)
        elif self.phase < 14 and self.is_jump:
            if self.is_left:
                self.image = player_img_j3
            else:
                self.image = pygame.transform.flip(player_img_j3, True, False)
        elif self.is_falling:
            if self.is_left:
                self.image = player_img_j4
            else:
                self.image = pygame.transform.flip(player_img_j4, True, False)
        elif self.is_just_fall:
            if self.is_left:
                self.image = player_img_j5
            else:
                self.image = pygame.transform.flip(player_img_j5, True, False)
            self.phase += 1
            if self.phase == 3:
                self.is_just_fall = False
        elif not self.is_falling and not self.is_just_fall:
            self.animation_going()


    def prepare_jump(self):
        if not self.is_jump and not self.is_falling and not self.is_just_fall:
            self.is_jump = True
            self.phase = 0
        # подготовка к прыжку

    def jump(self, obstacles_group):
        if self.is_jump:
            step = -15
            self.shadow.rect.centery += step
            if self.phase <= 2:
                if len(pygame.sprite.spritecollide(self.shadow, obstacles_group, False, None)) != 0:
                    self.is_jump = False
                self.shadow.rect.centery = self.rect.centery
            if self.phase > 2:
                if len(pygame.sprite.spritecollide(self.shadow, obstacles_group, False, None)) == 0:
                    self.rect.centery = self.shadow.rect.centery
                else:
                    self.shadow.rect.centery = self.rect.centery
                    self.is_jump = False
                self.shadow.rect.centerx += self.jump_direction
                if self.jump_direction != 0:
                    if len(pygame.sprite.spritecollide(self.shadow, obstacles_group, False, None)) == 0:
                        self.rect.centerx = self.shadow.rect.centerx
                    else:
                        self.shadow.rect.centerx = self.rect.centerx
                        self.jump_direction = 0
            self.phase += 1
            if self.phase == 13:
                self.is_jump = False
                self.phase = 0

    def update(self, x, obstacles_group):
        self.shadow.rect.center = self.rect.center
        pressed_button = pygame.key.get_pressed()
        if pressed_button[pygame.K_w] or pressed_button[pygame.K_SPACE] or pressed_button[pygame.K_UP]:
            self.prepare_jump()
            self.jump_direction = 0
            if pressed_button[pygame.K_a]:
                self.jump_direction = -x
            elif pressed_button[pygame.K_d]:
                self.jump_direction = x
        elif not self.is_jump:
            if pressed_button[pygame.K_a] or pressed_button[pygame.K_LEFT]:
                self.shadow.rect.centerx -= x
#                if self.shadow.rect.left < 0:
#                    self.shadow.rect.left = 0
                if len(pygame.sprite.spritecollide(self.shadow, obstacles_group, False, None)) == 0:
                    self.rect.center = self.shadow.rect.center
                else:
                    self.shadow.rect.center = self.rect.center
                if not self.is_left:
                    self.is_left = True
            elif pressed_button[pygame.K_d] or pressed_button[pygame.K_RIGHT]:
                self.shadow.rect.centerx += x
                if len(pygame.sprite.spritecollide(self.shadow, obstacles_group, False, None)) == 0:
                    self.rect.center = self.shadow.rect.center
                else:
                    self.shadow.rect.center = self.rect.center
#                if self.rect.right > WIDTH:
#                    self.rect.left = 0
                if self.is_left:
                   self.is_left = False
        self.animation_falling()
        self.jump(obstacles_group)



    def falling(self, obstacles_group):
        if not self.is_jump:
            buffer = self.is_falling
            self.shadow.rect.centery += 15
            if len(pygame.sprite.spritecollide(self.shadow, obstacles_group, False, None)) == 0:
                self.is_falling = True
                self.rect.center = self.shadow.rect.center
            elif len(pygame.sprite.spritecollide(self.shadow, obstacles_group, False, None)) != 0:
                self.shadow.rect.centery -= 10
                if len(pygame.sprite.spritecollide(self.shadow, obstacles_group, False, None)) == 0:
                    self.rect.center = self.shadow.rect.center
                    self.is_falling = True
                else:
                    self.is_falling = False
                    self.shadow.rect.center = self.rect.center
            if buffer and not self.is_falling:
                self.is_just_fall = True
                self.phase = 0
            self.animation_falling()

    def dying(self, group, *start_pos):
        if len(pygame.sprite.spritecollide(self, group, False, None)) == 0:
            pass
        else:
            self.rect.center = start_pos
            self.shadow.rect.center = self.rect.center


'''
    def __init__(self, pos, player_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image_left = player_img
        self.image_right = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.is_left = True
        self.is_jump = False
        self.speed = 2
        self.shadow = Images(player_img, pos)
        self.jump = False
        self.jump_p = 1
        self.jump_height = 19

    def update(self, obstacles_group):
        pressed_button = pygame.key.get_pressed()
        self.shadow.rect.center = self.rect.center
        if self.jump == True:
            self.pmuj()
        elif pressed_button[pygame.K_w]:
            self.jump = True
            self.jump_direction = 0
            if pressed_button[pygame.K_a]:
                self.jump_direction = -15
            elif pressed_button[pygame.K_d]:
                self.jump_direction = 15
        elif pressed_button[pygame.K_a] or pressed_button[pygame.K_LEFT]:
            self.shadow.rect.centerx -= self.speed
            if self.shadow.rect.left < 0:
                self.shadow.rect.left = 0
            if len(pygame.sprite.spritecollide(self.shadow, obstacles_group, False, None)) == 0:
                self.rect.center = self.shadow.rect.center
                if not self.is_left:
                    self.image = self.image_left
                    self.is_left = True
        elif pressed_button[pygame.K_d] or pressed_button[pygame.K_RIGHT]:
            self.shadow.rect.centerx += self.speed
            if len(pygame.sprite.spritecollide(self.shadow, obstacles_group, False, None)) == 0:
                self.rect.center = self.shadow.rect.center
                if self.is_left:
                    self.image = self.image_right
                    self.is_left = False

'''
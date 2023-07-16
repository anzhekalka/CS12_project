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

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, type, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = obstacles_list[type]
        self.rect = self.image.get_rect()
        self.rect.center = pos

class PLayer(pygame.sprite.Sprite):
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

    def update(self, obstacles_group):
        pressed_button = pygame.key.get_pressed()
        self.shadow.rect.center = self.rect.center
        if pressed_button[pygame.K_a] or pressed_button[pygame.K_LEFT]:
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


    def falling(self, object, tick_for_jump):
        if self.rect.bottom != object.rect.top and tick_for_jump == 0:
            if object.rect.top > self.rect.bottom:
                self.rect.bottom += 5
            elif object.rect.top < self.rect.bottom:
                self.rect.bottom = object.rect.top
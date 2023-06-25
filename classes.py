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
    def __init__(self, pos, player_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image_left = player_img
        self.image_right = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.is_left = True
        self.is_jump = False




    def update(self, x):
        pressed_button = pygame.key.get_pressed()

        if pressed_button[pygame.K_a] or pressed_button[pygame.K_LEFT]:
            self.rect.centerx -= x
            if self.rect.left < 0:
                self.rect.right = 1200
            if not self.is_left:
                self.image = self.image_left
                self.is_left = True
        elif pressed_button[pygame.K_d] or pressed_button[pygame.K_RIGHT]:
            self.rect.centerx += x
            if self.rect.right > 1200:
                self.rect.left = 0
            if self.is_left:
                self.image = self.image_right
                self.is_left = False

    def falling(self, object, tick_for_jump):
        if self.rect.bottom != object.rect.top and tick_for_jump == 0:
            if object.rect.top > self.rect.bottom:
                self.rect.bottom += 5
            elif object.rect.top < self.rect.bottom:
                self.rect.bottom = object.rect.top
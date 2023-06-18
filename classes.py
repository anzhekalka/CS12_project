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
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image_left = player_img
        self.image_right = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.is_left = True

    def update(self):
        pressed_button = pygame.key.get_pressed()
        if pressed_button[pygame.K_a]:
            self.rect.centerx -= 2
            if not self.is_left:
                self.image = self.image_left
                self.is_left = True
        elif pressed_button[pygame.K_d]:
            self.rect.centerx += 2
            if self.is_left:
                self.image = self.image_right
                self.is_left = False
        elif pressed_button[pygame.K_w]:
            self.rect.centery -= 2
        elif pressed_button[pygame.K_s]:
            self.rect.centery += 2

from resources import *


class Button(pygame.sprite.Sprite):
    def __init__(self, img_file, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img_file
        self.rect = self.image.get_rect()
        self.rect.center = pos


class PLayer(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pressed_button = pygame.key.get_pressed()
        print("update")
        if pressed_button[pygame.K_a]:
            self.rect.centerx -= 2
        elif pressed_button[pygame.K_d]:
            self.rect.centerx += 2
        elif pressed_button[pygame.K_w]:
            self.rect.centery -= 2
        elif pressed_button[pygame.K_s]:
            self.rect.centery += 2

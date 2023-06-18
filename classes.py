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
        self.image = image_to_put
        self.rect = self.image.get_rect()
        self.rect.center = pos




    def update(self, x):
        pressed_button = pygame.key.get_pressed()
        #print("update")
        if pressed_button[pygame.K_a] or pressed_button[pygame.K_LEFT]:
            self.rect.centerx -= x
            if self.rect.left < 0:
                self.rect.right = 1200
        elif pressed_button[pygame.K_d] or pressed_button[pygame.K_RIGHT]:
            self.rect.centerx += x
            if self.rect.right > 1200:
                self.rect.left = 0


        '''
        elif pressed_button[pygame.K_w]:
            self.rect.centery -= x
        elif pressed_button[pygame.K_s]:
            self.rect.centery += x
        '''
    def falling(self, object, tick_for_jump):
        if self.rect.bottom != object.rect.top and tick_for_jump == 0:
            if object.rect.top > self.rect.bottom:
                self.rect.bottom += 5
            elif object.rect.top < self.rect.bottom:
                self.rect.bottom = object.rect.top

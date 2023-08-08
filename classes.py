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
        self.image_left = image_to_put
        self.image_right = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.is_left = True
        self.is_jump = False
        self.phase = 0
        #self.shadow = Images(image_to_put, pos)

    def prepare_jump(self):
        self.is_jump = True
        self.phase = 0
        # подготовка к прыжку

    def jump(self):
        if self.is_jump:
            step = -5
            self.rect.centery += step
            self.phase += 1
            if self.phase == 10:
                self.is_jump = False
    def update(self, x):
        pressed_button = pygame.key.get_pressed()
        if pressed_button[pygame.K_w]:
            self.prepare_jump()
        elif pressed_button[pygame.K_a] or pressed_button[pygame.K_LEFT]:
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
        self.jump()

    def falling(self, object):
        if not self.is_jump:
            if self.rect.bottom != object.rect.top:
                if object.rect.top > self.rect.bottom:
                    self.rect.bottom += 15
                elif object.rect.top < self.rect.bottom:
                    self.rect.bottom = object.rect.top

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

    def falling(self, object, tick_for_jump):
        if self.rect.bottom != object.rect.top and tick_for_jump == 0:
            if object.rect.top > self.rect.bottom:
                self.rect.bottom += 5
            elif object.rect.top < self.rect.bottom:
                self.rect.bottom = object.rect.top

    def pmuj(self):
        if self.jump_p > 0:
            self.rect.y -= 5
            self.jump_p += 1
            self.rect.x += self.jump_direction
        elif self.jump_p < 0:
            self.rect.y += 10
            self.jump_p -= 1
            self.rect.x += self.jump_direction
        if self.jump_p == self.jump_height:
            self.jump_p = -1
        elif self.jump_p == -10:
            self.jump_p = 1
            self.jump = False
'''
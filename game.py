from pygame import *
from random import randint
from math import sin, sqrt
init()
class GameSrite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
        # self.mask = mask.from_surface(self.image)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSrite):
    def __init__(self, player_image, player_x, player_y, player_speed, size, controls=(K_UP, K_DOWN)):
            super().__init__(player_image, player_x, player_y, player_speed, size)
            self.controls = controls
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[self.controls[0]] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys_pressed[self.controls[1]] and self.rect.y < 630:
            self.rect.y += self.speed
window = display.set_mode((700, 500))
rocket1 = Player('border.png', 10, 10, 5, (20, 100))
rocket2 = Player('border.png', 20, 10, 5, (100, 500))
clock = time.Clock()
FPS = 40
game = True
finish = False
while game:
    frame_time = clock.tick(FPS)
    if finish != True:
        window.fill((200, 255, 255)) 
        rocket1.update()
        rocket2.reset()
        rocket1.update()
        rocket2.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
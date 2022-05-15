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
class Ball(GameSrite):

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.x < 0 or self.rect.x > 650:
            self.speed[0] *= -1
        if self.rect.y < 0 or self.rect.y > 450:
            self.speed[1] *= -1
class Player(GameSrite):
    def __init__(self, player_image, player_x, player_y, player_speed, size, controls=(K_UP, K_DOWN)):
            super().__init__(player_image, player_x, player_y, player_speed, size)
            self.controls = controls
            self.impulse = 0
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[self.controls[0]] and self.rect.y > 0:
            self.rect.y -= self.speed
            self.impulse = 0.5 *self.impulse - self.speed
        if keys_pressed[self.controls[1]] and self.rect.y < 400:
            self.rect.y += self.speed
            self.impulse = 0.5 *self.impulse + self.speed
window = display.set_mode((700, 500))
rocket1 = Player('bordercropped.png', 10, 10, 5, (20, 100), (K_w, K_s))
rocket2 = Player('bordercropped.png', 670, 10, 5, (20, 100), (K_UP, K_DOWN))
ball = Ball('basket_ballcropped.png', 100, 100, [3, 3], (50, 50))
clock = time.Clock()
FPS = 40
game = True
finish = False
while game:
    frame_time = clock.tick(FPS)
    if finish != True:
        window.fill((200, 255, 255)) 
        rocket1.update()
        rocket1.reset()
        rocket2.update()
        rocket2.reset()
        ball.update()
        ball.reset()
        if ball.rect.colliderect(rocket1.rect):
            ball.speed[0] *= -1
            ball.speed[1] += 0.3*rocket1.impulse
        if ball.rect.colliderect(rocket2.rect):
            ball.speed[0] *= -1
            ball.speed[1] += 0.3*rocket2.impulse
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()

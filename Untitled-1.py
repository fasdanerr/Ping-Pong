
from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def init(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.init(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Racket(GameSprite):
    def moveLeftRacket(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500-100:
            self.rect.y += self.speed
    def moveRightRacket(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500-100:
            self.rect.y += self.speed        

      

win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
window.fill((255, 255, 255))
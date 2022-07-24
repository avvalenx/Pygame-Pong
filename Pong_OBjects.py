import pygame
import random

class paddle():
    def __init__(self, width, length, color, x, y):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.color = color
        self.hitbox = (self.x, self.y, self.width, self.length)
        self.velocity = 12
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.length))

class ball():
    def __init__(self, radius, color, x, y, facing):
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.facing = facing
        self.xvel = 10
        self.served = False
        self.moving = False
        self.yvel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
    
    def serve(self):
        if self.served == False:
            self.served = True
            self.moving = True
            self.x += self.xvel*self.facing
            self.yvel = random.randint(-10, 10)
            self.y += self.yvel #figure out how to move up and down
    
    def move(self):
        self.x += self.xvel*self.facing
        self.y += self.yvel #figure out how to move up and down
    
    def bounce(self, paddle_y_value):
        multiplier = self.y - paddle_y_value - 60
        self.yvel += multiplier / 10
import pygame
import random
import math

WIDTH, HEIGHT = 700, 700

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
CYAN = (0, 255, 255)


class Spot:
    def __init__(self, index, WIDTH):
        self.val = 0
        self.row = index[0]
        self.column = index[1]
        self.x = self.row * 225 + 25
        self.y = self.column * 225 + 25
        self.width = 200

    def isEmpty(self):
        return self.val == 0

    def isCross(self):
        return self.val == 1

    def isDot(self):
        return self == -1

    def makeEmpty(self):
        self.val = 0

    def makeCross(self):
        self.val = 1

    def makeDot(self):
        self.val = -1

    def draw(self, window):
        pygame.draw.rect(window, WHITE, (self.x, self.y, self.width, self.width), 0)
        if self.val == 1:
            img = pygame.image.load("cross_icon.png")
            img = pygame.transform.scale(img, (150, 150))
            window.blit(img, (self.x + 25, self.y + 25))
        if self.val == -1:
            img = pygame.image.load("circle_icon.png")
            img = pygame.transform.scale(img, (150, 150))
            window.blit(img, (self.x + 25, self.y + 25))

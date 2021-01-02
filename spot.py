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


def getLineInformation(board):
    for i in range(3):
        sum_h, sum_v, sum_d1, sum_d2 = 0, 0, 0, 0
        for j in range(3):
            sum_v += board[i][j].val
            sum_h += board[j][i].val
            sum_d1 += board[j][j].val
            sum_d2 += board[j][2 - j].val
        if abs(sum_h) == 3 or abs(sum_v) == 3 or abs(sum_d1) == 3 or abs(sum_d2) == 3:
            if abs(sum_v) == 3:
                return (board[i][0].x + 100, board[i][0].y + 100), (
                    board[i][2].x + 100,
                    board[i][2].y + 100,
                )
            if abs(sum_h) == 3:
                return (board[0][i].x + 100, board[0][i].y + 100), (
                    board[2][i].x + 100,
                    board[2][i].y + 100,
                )
            if abs(sum_d1) == 3:
                return (125, 125), (575, 575)
            return (575, 125), (125, 575)


def result(board):
    total_empty_spot = 0
    for i in range(3):
        sum_h, sum_v, sum_d1, sum_d2 = 0, 0, 0, 0
        for j in range(3):
            if board[i][j].isEmpty():
                total_empty_spot += 1
            sum_h += board[i][j].val
            sum_v += board[j][i].val
            sum_d1 += board[j][j].val
            sum_d2 += board[j][2 - j].val
        if sum_h == 3 or sum_v == 3 or sum_d1 == 3 or sum_d2 == 3:
            return 1
        if sum_h == -3 or sum_v == -3 or sum_d1 == -3 or sum_d2 == -3:
            return -1
    if not total_empty_spot:
        return 0


def draw(window, board, WIDTH):
    window.fill(BLACK)
    for row in board:
        for spot in row:
            spot.draw(window)
    pygame.display.update()


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

import random
import math
import pygame
from spot import Spot

pygame.init()

WIDTH, HEIGHT = 700, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC-TAC-TOE AI")


RED = (255, 0, 0)
BLACK = (0, 0, 0)


def draw(window, board, WIDTH):
    window.fill(BLACK)
    for row in board:
        for spot in row:
            spot.draw(window)
    pygame.display.update()


def getSpotLocation(position, board):
    x, y = position
    for row in board:
        for spot in row:
            if (
                spot.x <= x <= spot.x + spot.width
                and spot.y <= y <= spot.y + spot.width
            ):
                return (spot.row, spot.column)
    return False


def makeBoard(window, WIDTH):
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(Spot((i, j), WIDTH))
        board.append(row)
    return board


def reset(window, board, start, WIDTH):
    board = makeBoard(window, WIDTH)
    draw(window, board, WIDTH)
    main(window, WIDTH, start)


def turn(toggle):
    return 1 if toggle == -1 else -1


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


def gameOver(board):
    if result(board) != None:
        return True


def main(window, WIDTH, start):
    toggle = start
    run = True
    board = makeBoard(window, WIDTH)
    draw(window, board, WIDTH)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                spot = getSpotLocation(position, board)
                try:
                    row, column = spot
                    if board[row][column].isEmpty():
                        if toggle == 1:
                            board[row][column].makeCross()
                        else:
                            board[row][column].makeDot()
                        toggle = turn(toggle)
                        draw(window, board, WIDTH)
                    if gameOver(board):
                        pygame.time.delay(500)
                        if result(board) != 0:
                            start_pos, end_pos = getLineInformation(board)
                            pygame.draw.line(window, RED, start_pos, end_pos, 20)
                            pygame.display.update()
                            pygame.time.delay(1000)
                        reset(window, board, start, WIDTH)
                except Exception as e:
                    print(e)
                    print("Clicked outside available spot")
    pygame.quit()


main(window, WIDTH, 1)

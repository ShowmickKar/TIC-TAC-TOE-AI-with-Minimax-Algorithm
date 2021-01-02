import random
import math
import pygame
from spot import Spot, draw, result, getLineInformation
from minimax import decideBestMove

pygame.init()

WIDTH, HEIGHT = 700, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC-TAC-TOE AI")


BLACK = (0, 0, 0)


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


def reset(window, board, start, WIDTH, current_player):
    board = makeBoard(window, WIDTH)
    draw(window, board, WIDTH)
    main(window, WIDTH, start, turn(current_player))


def turn(toggle):
    return 1 if toggle == -1 else -1


def gameOver(board):
    if result(board) != None:
        return True


def main(window, WIDTH, start, current_player):
    AI = current_player
    toggle = start
    run = True
    board = makeBoard(window, WIDTH)
    draw(window, board, WIDTH)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if AI > 0:
                row, column = decideBestMove(board, current_player)
                if row == None or result(board) == 0:
                    pygame.time.delay(1000)
                    reset(window, board, start, WIDTH, current_player)
                if toggle == 1:
                    board[row][column].makeCross()
                else:
                    board[row][column].makeDot()
                AI = turn(AI)
                toggle = turn(toggle)
                draw(window, board, WIDTH)
                if gameOver(board):
                    pygame.time.delay(500)
                    if result(board) != 0:
                        start_pos, end_pos = getLineInformation(board)
                        pygame.draw.line(window, BLACK, start_pos, end_pos, 20)
                        pygame.display.update()
                        pygame.time.delay(1000)
                    reset(window, board, start, WIDTH, current_player)
                continue
            if AI < 0 and pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                spot = getSpotLocation(position, board)
                try:
                    if result(board) == 0:
                        reset(window, board, start, WIDTH, current_player)
                    row, column = spot
                    if board[row][column].isEmpty():
                        if toggle == 1:
                            board[row][column].makeCross()
                        else:
                            board[row][column].makeDot()
                        toggle = turn(toggle)
                        AI = turn(AI)
                        draw(window, board, WIDTH)
                    if gameOver(board):
                        pygame.time.delay(500)
                        if result(board) != 0:
                            start_pos, end_pos = getLineInformation(board)
                            pygame.draw.line(window, BLACK, start_pos, end_pos, 20)
                            pygame.display.update()
                            pygame.time.delay(1000)
                        reset(window, board, start, WIDTH, current_player)
                except Exception as e:
                    print(e)
                    print("Clicked outside available spot")
    pygame.quit()


main(window, WIDTH, 1, -1)
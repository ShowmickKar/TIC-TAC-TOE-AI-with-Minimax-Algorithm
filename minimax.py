import random
import math
import pygame
from spot import Spot, result


def decideBestMove(board, current_player):
    print(current_player)
    bestScore = -math.inf
    row, column = None, None
    for i in range(3):
        for j in range(3):
            if board[i][j].isEmpty():
                board[i][j].val = current_player
                score = minimax(board, 0, False, current_player)
                board[i][j].val = 0
                if score > bestScore:
                    bestScore = score
                    row, column = i, j
    return row, column


def minimax(board, depth, is_maximizing, current_player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if result(board) != None:
        score = result(board) * current_player
        return score
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j].isEmpty():
                    board[i][j].val = current_player
                    score = minimax(board, depth + 1, not is_maximizing, current_player)
                    board[i][j].val = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j].isEmpty():
                    board[i][j].val = -current_player
                    score = minimax(board, depth + 1, not is_maximizing, current_player)
                    board[i][j].val = 0
                    best_score = min(score, best_score)
        return best_score
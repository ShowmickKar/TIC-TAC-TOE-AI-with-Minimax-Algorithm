import random
import math
import pygame
from spot import Spot


def decideBestMove(board, computer_move, result):
    all_empty = True
    bestScore = -math.inf
    row, column = None, None
    for i in range(3):
        for j in range(3):
            if board[i][j].isEmpty():
                pass
            else:
                all_empty = False
                break
    if all_empty:
        return random.choice([(0, 0), (0, 2), (2, 0), (2, 2)])
    for i in range(3):
        for j in range(3):
            if board[i][j].isEmpty():
                board[i][j].val = computer_move
                score = minimax(board, 0, False, computer_move, result)
                board[i][j].val = 0
                if score > bestScore:
                    bestScore = score
                    row, column = i, j
    return row, column


def minimax(board, depth, is_maximizing, computer_move, result):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if result() != None:
        score = result() * computer_move
        return score
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j].isEmpty():
                    board[i][j].val = computer_move
                    score = minimax(
                        board, depth + 1, not is_maximizing, computer_move, result
                    )
                    board[i][j].val = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j].isEmpty():
                    board[i][j].val = -computer_move
                    score = minimax(
                        board, depth + 1, not is_maximizing, computer_move, result
                    )
                    board[i][j].val = 0
                    best_score = min(score, best_score)
        return best_score

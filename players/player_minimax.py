#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from player import Player
from util import *

# ==========================================
# Player Minimax
# ==========================================

class MinimaxPlayer(Player):

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, symbol):
        super(MinimaxPlayer, self).__init__(symbol)

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):
        (next_move, _) = self.minimax(2, board, self.me())
        return next_move

    def minimax(self, level, board, player):
        next_move  = None
        best_score = -99999 if player == self.me() else 99999

        cells = find_empty_cells(board)

        if level == 0:
            (score, wins) = self.score(board)

            for x in cells:
                if x not in wins:
                    return (x, score)

            return (cells[0], score)

        for x in cells:
            _cells    = board[:]
            _cells[x] = player

            inverse_player = self.me() if player == self.opp() else self.opp()

            (_, score) = self.minimax(level - 1, _cells, inverse_player)

            if player == self.me():
                if score > best_score:
                    best_score = score
                    next_move = x

            elif player == self.opp():
                score = score * -1

                if score < best_score:
                    best_score = score
                    next_move = x

        return (next_move, best_score)

    def score(self, board):
        score = 1
        move_win = []

        for i in board:
            (winner, move) = find_winner(board)

            if winner != None:
                move_win.append(i)

                if len(move_win) == 1:
                    score = 1
                elif len(move_win) == 2:
                    score = 10
                else:
                    score = 100

                if winner != self.me():
                    score = score * -1

        return (score, move_win)
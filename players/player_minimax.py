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
        best_score = -99999

        cells = find_empty_cells(board)

        for x in cells:
            _cells = board[:]
            _cells[x] = self.me()

            (winner, moves) = find_winner(_cells)

            if winner == self.me():
                score = self.score(moves)

                if score > best_score:
                    best_score = score
                    next_move = x

            _cells[x] = self.opp()
            (winner, moves) = find_winner(_cells)

            if winner == self.opp():
                score = self.score(moves)

                if score > best_score:
                    best_score = score
                    next_move = x

        if next_move == None:
            next_move = cells[0]

        return (next_move, best_score)

    def score(self, moves):
        len_m = len(moves)

        print(`moves`)

        return len_m

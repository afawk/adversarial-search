#!/usr/bin/env python
# Four spaces as indentation [no tabs]

import unittest
from common import *
from util import *
from tictactoe import *
from players import *

PLAYS = 10

RANDOM = "random"
MINIMAX = "minimax"
ALPHABETA = "alphabeta"

PLAYERS = { str(c): c for c in vars()["Player"].__subclasses__() }

def percentage(wins, games):
    return float(wins) / float(games) * 100

# ==========================================
# Test TicTacToe
# ==========================================

class Test_TicTacToe(unittest.TestCase):

    # ------------------------------------------
    # Create game
    # ------------------------------------------

    def versus(self, playerO_name, playerX_name, rounds, time_per_round=0):

        wins = 0
        losses = 0
        draws = 0
        errors = 0

        @timelimit(time_per_round)
        def round_exec(playerO_name, playerX_name):
            playerO = PLAYERS[playerO_name](O)
            playerX = PLAYERS[playerX_name](X)
            game = TicTacToe(playerO, playerX, False)
            while game.winner == None:
                game.update()
            return DRAW if game.winner == DRAW else game.winner.symbol

        for round in range(rounds):
            try:
                winner = round_exec(playerO_name, playerX_name)
                if winner == O:
                    wins += 1
                elif winner == X:
                    losses += 1
                elif winner == DRAW:
                    draws += 1
            except Exception, e:
                errors += 1

        return (wins, losses, draws, errors)

    # ------------------------------------------
    # Random Vs Minimax
    # ------------------------------------------

    def test_random_vs_minimax(self):
        wins, losses, draws, errors = self.versus(RANDOM, MINIMAX, PLAYS)

        print "Random VS Minimax results:"
        print "  Wins: %f (%f%%)" % ( wins, percentage(wins, PLAYS) )
        print "  Losses: %f (%f%%)" % ( losses, percentage(losses, PLAYS) )
        print "  Draws: %f (%f%%)" % ( draws, percentage(draws, PLAYS) )

        # Random losses == Minimax wins
        self.assertGreaterEqual(percentage(losses, PLAYS), 0.5)
        self.assertEqual(errors, 0)

if __name__ == "__main__":
    unittest.main(verbosity=False)
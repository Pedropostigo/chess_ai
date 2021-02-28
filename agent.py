import numpy as np


class Agent(object):

    def __init__(self):
        pass

    def move(self, board):
        # for now, just implement random move
        random_move = np.random.choice(list(board.legal_moves))
        return random_move
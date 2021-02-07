import numpy as np

import panel as pn
import chess

class ChessUI(object):

    def __init__(self):
        self.board = chess.Board()

    def _random_move(self, target, event):
        random_move = np.random.choice(list(self.board.legal_moves))
        self.board.push(random_move)
        target.object = self.board

    def show(self):

        board_pane = pn.panel(self.board)
        random_move_button = pn.widgets.Button(name = "random move")
        random_move_button.link(board_pane,
                        callbacks = {'value': self._random_move})

        panel = pn.Column(board_pane, random_move_button)
        panel.show()

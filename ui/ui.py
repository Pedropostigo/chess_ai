import numpy as np

import panel as pn
import chess

class ChessUI(object):

    def __init__(self, white_agent, black_agent):
        self.board = chess.Board()
        self.white_agent = white_agent
        self.black_agent = black_agent

    def _move(self, target, event):
        
        # check which turn to move, and perform the move of the agent
        if self.board.turn == chess.WHITE:
            next_move = self.white_agent.move(self.board)
        elif self.board.turn == chess.BLACK:
            next_move = self.black_agent.move(self.board)

        # push the move to the board
        self.board.push(next_move)
        target.object = self.board

    def show(self):

        board_pane = pn.panel(self.board)
        next_move_button = pn.widgets.Button(name = "Next move")
        next_move_button.link(board_pane,
                        callbacks = {'value': self._move})

        panel = pn.Column(board_pane, next_move_button)
        panel.show()

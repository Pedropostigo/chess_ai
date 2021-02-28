from ui.ui import ChessUI
from agent import Agent

chess_ui = ChessUI(white_agent = Agent(),
                    black_agent= Agent())
chess_ui.show()
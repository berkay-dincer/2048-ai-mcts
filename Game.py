from Board import Board


class Game:
    def __init__(self):
        pass

    def play_random_with_state(self, board_state):
        """Start playing from the given board state and return score"""
        board = Board(board_state)

        while True:
            board.move_board_random()
            board.add_random_tile()
            if board.is_cells_available() is False and board.is_match_available() is False:
                board_states, score = board.get_board_states_and_score()
                return score

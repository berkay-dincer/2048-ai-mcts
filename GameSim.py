from Board import Board
from BoardStateTracker import BoardStateTracker
import random

NUMBER_OF_ITERATIONS = 10000


def get_random_direction():
    return directions[random.randint(0, len(directions) - 1)]


directions = ['up', 'down', 'right', 'left']
state_tracker = BoardStateTracker()
for i in range(0, NUMBER_OF_ITERATIONS):
    board = Board()
    while True:
        board.move_board(get_random_direction())
        board.add_random_tile()
        if board.is_cells_available() is False:
            print 'game over, score:' + str(board.score)
            board_states, score = board.get_board_states_and_score()
            state_tracker.save_board_states(board_states, score)
            break

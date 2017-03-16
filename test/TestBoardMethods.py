import unittest
from src.Board import Board


class TestBoardMethods(unittest.TestCase):
    def test_move_right(self):
        current_state = [[0, 0, 0, 2],
                         [0, 0, 0, 2],
                         [0, 0, 2, 2],
                         [0, 0, 0, 2]]

        test_board = Board(current_state)
        test_board.move_board('right')
        next_state = test_board.board

        true_next_state = [[0, 0, 0, 2],
                           [0, 0, 0, 2],
                           [0, 0, 0, 4],
                           [0, 0, 0, 2]]

        self.assertEqual(next_state, true_next_state)

    def test_move_right_restricted(self):
        current_state = [[0, 0, 0, 2],
                         [0, 0, 0, 2],
                         [0, 0, 2, 4],
                         [0, 0, 2, 4]]

        test_board = Board(current_state)
        test_board.move_board('right')
        next_state = test_board.board

        self.assertEqual(next_state, current_state)

    def test_move_left(self):
        current_state = [[0, 0, 0, 2],
                         [0, 0, 0, 2],
                         [0, 0, 2, 2],
                         [0, 0, 0, 2]]

        test_board = Board(current_state)
        test_board.move_board('left')
        next_state = test_board.board

        true_next_state = [[2, 0, 0, 0],
                           [2, 0, 0, 0],
                           [4, 0, 0, 0],
                           [2, 0, 0, 0]]

        self.assertEqual(next_state, true_next_state)

    def test_move_left_restricted(self):
        current_state = [[2, 0, 0, 0],
                         [2, 0, 0, 0],
                         [4, 2, 0, 0],
                         [4, 2, 0, 0]]

        test_board = Board(current_state)
        test_board.move_board('left')
        next_state = test_board.board

        self.assertEqual(next_state, current_state)

    def test_move_up(self):
        current_state = [[0, 0, 0, 2],
                         [0, 0, 0, 2],
                         [0, 0, 2, 2],
                         [0, 0, 0, 2]]

        test_board = Board(current_state)
        test_board.move_board('up')
        next_state = test_board.board

        true_next_state = [[0, 0, 2, 4],
                           [0, 0, 0, 4],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0]]

        self.assertEqual(next_state, true_next_state)

    def test_move_up_restricted(self):
        current_state = [[0, 2, 4, 4],
                         [0, 0, 2, 2],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]

        test_board = Board(current_state)
        test_board.move_board('up')
        next_state = test_board.board

        self.assertEqual(next_state, current_state)

    def test_move_down(self):
        current_state = [[0, 0, 0, 2],
                         [0, 0, 0, 2],
                         [0, 0, 2, 2],
                         [0, 0, 0, 2]]

        test_board = Board(current_state)
        test_board.move_board('down')
        next_state = test_board.board

        true_next_state = [[0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 4],
                           [0, 0, 2, 4]]

        self.assertEqual(next_state, true_next_state)

    def test_move_down_restricted(self):
        current_state = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 2, 2],
                         [0, 2, 4, 4]]

        test_board = Board(current_state)
        test_board.move_board('down')
        next_state = test_board.board

        self.assertEqual(next_state, current_state)

suite = unittest.TestLoader().loadTestsFromTestCase(TestBoardMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
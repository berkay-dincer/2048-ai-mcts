import random
import sys


class Board:
    def __init__(self, board = None):
        self.size = 4
        self.start_tiles = 2
        self.score = 0
        self.board_tracker = list()
        if board is None:
            self.board = [[0 for x in range(self.size)] for y in range(self.size)]
            for i in range(self.start_tiles):
                self.add_random_tile()
        else:
            self.board = board
        self._track_board_state()

    def add_random_tile(self):
        if self.is_cells_available():
            value_to_add = self.generate_random_value()
            available_cells = self.get_available_cells()
            rand_index = random.randint(0, len(available_cells) - 1)
            chosen_cell = available_cells[rand_index]
            self.board[chosen_cell[0]][chosen_cell[1]] = value_to_add

    def is_cells_available(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return True
        return False

    def get_available_cells(self):
        width = len(self.board)
        found = []
        position = 0
        for row in self.board:
            for value in row:
                if value == 0:
                    found.append((position // width, position % width))
                position += 1
        return found

    @staticmethod
    def generate_random_value():
        rand_int = random.randint(1, 10)
        value_to_add = 2
        if rand_int > 9:
            value_to_add = 4
        return value_to_add

    def move_board(self, direction):
        merged_lists = list()
        lists_to_merge = self._get_lists_to_merge(direction)
        for i in range(0, self.size):
            if direction is 'down' or direction is 'right':
                merged_lists.append(list(reversed(self._merge(lists_to_merge[i]))))
            else:
                merged_lists.append(self._merge(lists_to_merge[i]))

        self.board = self._reassemble_vertical_lists(merged_lists, direction)
        self._track_board_state()

    def move_board_random(self):
        directions = ['up', 'down', 'right', 'left']
        direction = directions[random.randint(0, len(directions) - 1)]
        merged_lists = list()
        lists_to_merge = self._get_lists_to_merge(direction)
        for i in range(0, self.size):
            if direction is 'down' or direction is 'right':
                merged_lists.append(list(reversed(self._merge(lists_to_merge[i]))))
            else:
                merged_lists.append(self._merge(lists_to_merge[i]))

        self.board = self._reassemble_vertical_lists(merged_lists, direction)
        self._track_board_state()

    def _reassemble_vertical_lists(self, merged_lists, direction):
        if direction is 'down' or direction is 'up':
            tuples = zip(*merged_lists)
            for i in range(0, self.size):
                merged_lists[i] = list(tuples[i])
        return merged_lists

    def _merge(self, list_to_merge):
        non_zeros_removed = []
        result = []
        merged = False
        for value in list_to_merge:
            if value != 0:
                non_zeros_removed.append(value)

        while len(non_zeros_removed) != len(list_to_merge):
            non_zeros_removed.append(0)

        # Double sequential tiles if same value
        for number in range(0, len(non_zeros_removed) - 1):
            if non_zeros_removed[number] == non_zeros_removed[number + 1] and merged is False:
                result.append(non_zeros_removed[number] * 2)
                merged = True
                self.score += non_zeros_removed[number] * 2
            elif non_zeros_removed[number] != non_zeros_removed[number + 1] and merged is False:
                result.append(non_zeros_removed[number])
            elif merged:
                merged = False

        if non_zeros_removed[-1] != 0 and merged is False:
            result.append(non_zeros_removed[-1])

        while len(result) != len(non_zeros_removed):
            result.append(0)

        return result

    def _get_lists_to_merge(self, direction):
        if direction is "up" or direction is "down":
            lists_to_merge = self._get_columns()
        else:
            lists_to_merge = self._get_rows()
        return lists_to_merge

    def _get_rows(self):
        rows = list()
        for row in self.board:
            rows.append(row)
        return rows

    def _get_columns(self):
        columns = list()
        for i in range(self.size):
            column = list()
            for row in self.board:
                column.append(row[i])
            columns.append(column)
        return columns

    def print_board(self):
        for row in self.board:
            for value in row:
                sys.stdout.write('|' + str(value) + '|')
            sys.stdout.write("\n")
        sys.stdout.write("----\n")

    def _track_board_state(self):
        self.board_tracker.append(self.board)

    def get_board_states_and_score(self):
        return self.board_tracker, self.score

    def simulate_next_move(self, direction):
        """Simulates next move and returns the resulting board"""
        merged_lists = list()
        lists_to_merge = self._get_lists_to_merge(direction)
        for i in range(0, self.size):
            if direction is 'down' or direction is 'right':
                merged_lists.append(list(reversed(self._merge(lists_to_merge[i]))))
            else:
                merged_lists.append(self._merge(lists_to_merge[i]))

        return self._reassemble_vertical_lists(merged_lists, direction)

    def is_match_available(self):
        for i in range(0,len(self.board)):
            for j in range(0, len(self.board[i])):
                current_cell = self.board[i][j]
                if i != 0:
                    up_cell = self.board[i-1][j]
                    if current_cell == up_cell:
                        return True
                if i != len(self.board[i])-1:
                    down_cell = self.board[i+1][j]
                    if current_cell == down_cell:
                        return True
                if j != 0:
                    left_cell = self.board[i][j-1]
                    if current_cell == left_cell:
                        return True
                if j != len(self.board)-1:
                    right_cell = self.board[i][j+1]
                    if current_cell == right_cell:
                        return True
        return False

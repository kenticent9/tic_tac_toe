"""This is a module for keeping the board class."""


class Board:
    """Stores the current state of the game and last move (symbol and
    position)."""

    def __init__(self, state):
        """Initialize a new board with the state and last symbol and
        pos attributes set to None, as no moves are made yet."""
        self.cur_state = state
        self.last_symbol = None
        self.last_pos = None

    def get_available_poss(self):
        """Return the available for a move positions."""
        return [(i, j) for i in range(3) for j in range(3)
                if self.cur_state[i][j] == " "]

    def make_move(self, x, y):
        """Make a move taking into account the last symbol."""
        if not (0 <= x < 3 and 0 <= y < 3) or self.cur_state[x][y] != " ":
            raise ValueError
        self.cur_state[x][y] = self.last_symbol = "o" \
            if self.last_symbol == "x" else "x"
        self.last_pos = (x, y)

    def check_state(self):
        """Check the current state on the playing field: if someone
        won, if draw, or the result is not determined."""
        for i in range(3):
            # Check rows
            if all(symbol == self.cur_state[i][0] != " "
                   for symbol in self.cur_state[i]):
                return 1 if self.cur_state[i][0] == "o" else -1
            # Check columns
            if self.cur_state[0][i] == self.cur_state[0][i] != " " \
                    and self.cur_state[1][i] == self.cur_state[0][i] \
                    and self.cur_state[2][i] == self.cur_state[0][i]:
                return 1 if self.cur_state[0][i] == "o" else -1
        # Check diagonals
        if self.cur_state[0][0] == self.cur_state[1][1] \
                == self.cur_state[2][2] != " " or self.cur_state[0][2] == \
                self.cur_state[1][1] == self.cur_state[2][0] != " ":
            return 1 if self.cur_state[2][2] == "o" else -1
        # Check if draw
        if not self.get_available_poss():
            return 0

    def __str__(self):
        """Return a user-friendly representation of the board."""
        return "\n—+—+—\n".join("|".join(self.cur_state[i]) for i in range(3))

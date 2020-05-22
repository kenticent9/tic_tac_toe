"""This is a module for keeping the Node class."""


class Node:
    """Stores the board and references to the left and right nodes."""

    def __init__(self, board):
        """Initialize a new node with the board and left and right
        attributes set to None."""
        self.board = board
        self.left = None
        self.right = None

import copy
import random

from tic_tac_toe.btnode import Node


class Tree:
    """This is a class for finding the best move by randomly building
    a binary tree of game outcomes and comparing the summary of wins to
    which the left and right nodes of the root lead using recursion."""

    def __init__(self, init_board):
        """Initialize the initial state of the board and randomly build
        a binary tree of game outcomes."""
        self._root = Node(init_board)

        def _build_tree(root):
            available_poss = root.board.get_available_poss()
            if not available_poss:
                return None
            x, y = random.choice(available_poss)
            lchild = Node(copy.deepcopy(root.board))
            lchild.board.make_move(x, y)

            available_poss = lchild.board.get_available_poss()
            if not available_poss:
                return None
            x, y = random.choice(available_poss)
            rchild = Node(copy.deepcopy(root.board))
            rchild.board.make_move(x, y)

            root.left, root.right = lchild, rchild
            _build_tree(lchild)
            _build_tree(rchild)

        _build_tree(self._root)

    def find_best_move(self):
        """Find the best move comparing the summary of wins to which
        the left and right nodes of the root lead using recursion."""

        def _calculate_points(root):
            if root is None:
                return 0
            if root.board.check_state() is None:
                points = _calculate_points(root.left) \
                         + _calculate_points(root.right)
                return points
            return root.board.check_state()

        left_points = _calculate_points(self._root.left)
        right_points = _calculate_points(self._root.right)
        if left_points > right_points:
            return self._root.left.board.last_pos
        return self._root.right.board.last_pos

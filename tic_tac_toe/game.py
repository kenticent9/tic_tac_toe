"""This is a module for playing Tic-Tac-Toe."""
from tic_tac_toe.board import Board
from tic_tac_toe.btree import Tree


def main():
    """Play Tic-Tac-Toe."""
    board = Board([[" " for _ in range(3)] for _ in range(3)])
    print("Enter a pair of coordinates separated by space in range 3 "
          "(e.g, 1 1).")
    while board.check_state() is None:
        print(board)
        coords = input("> ").strip().split()
        try:
            x, y = (int(coord) for coord in coords)
            board.make_move(x, y)
        except ValueError:
            print("Enter a valid pair of coordinates.")
            continue
        tree = Tree(board)
        x, y = tree.find_best_move()
        board.make_move(x, y)
    if board.check_state() == -1:
        print("You won!")
    elif board.check_state() == 0:
        print("Draw!")
    else:
        print("Computer won!")


if __name__ == '__main__':
    main()
